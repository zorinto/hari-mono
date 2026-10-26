#!/bin/sh
# Zip dist/ into release archives. Every archive carries the OFL licence; the Nerd Font one also
# carries the licences of the icon sets patched in.
set -e
HERE=$(cd "$(dirname "$0")" && pwd)
OUT=$HERE/dist
PATCHER=$(ls -d "${CACHE:-$HERE/.cache}"/nerd-fonts-* | head -1)
STAGE=$OUT/stage
rm -rf "$STAGE" "$OUT"/release && mkdir -p "$OUT/release"

mkdir -p "$STAGE/HariMono/Hinted" "$STAGE/HariMono/Unhinted"
cp "$OUT"/ttf/*.ttf "$STAGE/HariMono/Hinted/"
cp "$OUT"/ttf-unhinted/*.ttf "$STAGE/HariMono/Unhinted/"

mkdir -p "$STAGE/HariMono-NerdFont/icon-licences"
cp "$OUT"/nerd-font/*.ttf "$STAGE/HariMono-NerdFont/"
for f in "$PATCHER"/src/glyphs/*/LICENSE*; do
	cp "$f" "$STAGE/HariMono-NerdFont/icon-licences/$(basename "$(dirname "$f")")-$(basename "$f")"
done
cat > "$STAGE/HariMono-NerdFont/icon-licences/README.txt" <<'EOF'
The icons in these fonts were added with the Nerd Fonts patcher (https://www.nerdfonts.com, MIT licence).
Each icon set keeps its own licence; the files in this folder are copied from the patcher's src/glyphs.
The Hari Mono glyphs themselves are under the SIL Open Font License 1.1 (see LICENSE).
EOF

mkdir -p "$STAGE/HariMono-Web"
cp "$OUT"/woff2/*.woff2 "$STAGE/HariMono-Web/"
for style in Regular:400:normal Italic:400:italic Medium:500:normal MediumItalic:500:italic SemiBold:600:normal SemiBoldItalic:600:italic Bold:700:normal BoldItalic:700:italic; do
	IFS=: read -r name weight slope <<EOF
$style
EOF
	printf '@font-face {\n  font-family: "Hari Mono";\n  src: url("HariMono-%s.woff2") format("woff2");\n  font-weight: %s;\n  font-style: %s;\n  font-display: swap;\n}\n' \
		"$name" "$weight" "$slope" >> "$STAGE/HariMono-Web/hari-mono.css"
done

for pkg in HariMono HariMono-NerdFont HariMono-Web; do
	cp "$HERE/LICENSE" "$STAGE/$pkg/"
	(cd "$STAGE" && zip -qr "$OUT/release/$pkg.zip" "$pkg")
done
rm -rf "$STAGE"
ls -l "$OUT/release"
