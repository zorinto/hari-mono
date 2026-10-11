"""Post-process a Hari Mono build: fit a few symbols to the sizes in data/symbol-fit.json.

Narrow symbols are taken from the narrower donor build (same stroke weight), then moved so their
bounding-box centre sits on the target's. No outline is scaled, except the hyphen, which is narrowed
along its stroke so its thickness is unchanged.

Targets are upright. For a slanted style, pass the unprocessed upright font of the same weight: each
glyph's horizontal shift from the slant is taken from that pair and added to the target.

Usage: uv run --with fonttools postprocess.py <font.ttf> <donor.ttf> <symbol-fit.json> <regular|bold> <out.ttf> [upright.ttf]
"""

import json
import sys

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont

# Character -> source of its outline ("self" keeps the original and only moves it).
PLAN = {
    "(": "donor",
    ")": "donor",
    "[": "donor",
    "]": "donor",
    "{": "donor",
    "}": "donor",
    "<": "donor",
    ">": "donor",
    "^": "donor",
    "`": "donor",
    "~": "donor",
    "_": "self",
    "-": "self",
    "/": "self",
    "\\": "self",
    "|": "self",
    "*": "self",
}
STRETCH_X = {"-"}  # horizontal strokes only: scale x to the target width


def bounds(glyph_set, name):
    pen = BoundsPen(glyph_set)
    glyph_set[name].draw(pen)
    return pen.bounds


def main(font_path, donor_path, fit_path, weight, out_path, upright_path=None):
    font = TTFont(font_path)
    upright = TTFont(upright_path) if upright_path else None
    sources = {"self": font, "donor": TTFont(donor_path)}
    with open(fit_path) as f:
        targets = json.load(f)[weight]
    cmap = font.getBestCmap()
    glyf, hmtx = font["glyf"], font["hmtx"]
    new = {}
    for ch, source_key in PLAN.items():
        source = sources[source_key]
        gs = source.getGlyphSet()
        src = source.getBestCmap()[ord(ch)]
        x0, y0, x1, y1 = bounds(gs, src)
        tx0, tx1, ty0, ty1 = targets[ch]
        sx = (tx1 - tx0) / (x1 - x0) if ch in STRETCH_X else 1.0
        slant = 0.0
        if upright:
            own = bounds(font.getGlyphSet(), cmap[ord(ch)])
            up = bounds(upright.getGlyphSet(), upright.getBestCmap()[ord(ch)])
            slant = (own[0] + own[2]) / 2 - (up[0] + up[2]) / 2
        dx = (tx0 + tx1) / 2 + slant - sx * (x0 + x1) / 2
        dy = (ty0 + ty1) / 2 - (y0 + y1) / 2
        # Donor glyphs may be composites; copy plain outlines only.
        rec = DecomposingRecordingPen(gs)
        gs[src].draw(rec)
        pen = TTGlyphPen(None)
        rec.replay(TransformPen(pen, (sx, 0, 0, 1, dx, dy)))
        new[cmap[ord(ch)]] = pen.glyph()
    # Replace after reading, so sources never see half-edited glyphs.
    for name, glyph in new.items():
        glyph.recalcBounds(glyf)
        glyf[name] = glyph
        hmtx[name] = (hmtx[name][0], glyph.xMin)
    # Iosevka repeats the OVERLAP_SIMPLE flag (bit 6) past the first point; once fontTools recompiles
    # the glyphs, Chrome's sanitiser (OTS) rejects the whole font. The spec only allows it on point 0.
    for name in font.getGlyphOrder():
        g = glyf[name]
        if g.numberOfContours > 0:
            for i in range(1, len(g.flags)):
                g.flags[i] &= ~0x40
    font.save(out_path)


if __name__ == "__main__":
    main(*sys.argv[1:7])
