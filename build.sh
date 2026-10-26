#!/bin/sh
# Build Hari Mono into dist/: Iosevka build (font + narrow donor), symbol fitting, hinting, WOFF2,
# and a Nerd Font version. Needs git, pnpm, uv; ttfautohint and fontforge for the hinted and Nerd Font sets.
set -e
HERE=$(cd "$(dirname "$0")" && pwd)
IOSEVKA_REF=v34.9.0
NERD_REF=v3.5.1
CACHE=${CACHE:-$HERE/.cache}
IOSEVKA=$CACHE/iosevka-$IOSEVKA_REF
PATCHER=$CACHE/nerd-fonts-$NERD_REF
OUT=$HERE/dist
STYLES="Regular Italic Medium MediumItalic SemiBold SemiBoldItalic Bold BoldItalic"

ots() { uv run --with opentype-sanitizer python -m ots "$1" /dev/null > /dev/null || { echo "OTS rejected $1" >&2; exit 1; }; }

# 1. Iosevka at a pinned release, with pnpm linking its workspace packages.
if [ ! -d "$IOSEVKA" ]; then
	git clone --quiet --depth 1 --branch "$IOSEVKA_REF" https://github.com/be5invis/Iosevka.git "$IOSEVKA"
	printf 'packages:\n  - packages/*\n  - tools/*\nlinkWorkspacePackages: true\nnodeLinker: hoisted\n' > "$IOSEVKA/pnpm-workspace.yaml"
fi
cp "$HERE/private-build-plans.toml" "$IOSEVKA/"
(cd "$IOSEVKA" && pnpm install --silent && pnpm exec verda -f verdafile.mjs \
	ttf-unhinted::HariMono ttf-unhinted::HariMonoDonor --jCmd="${JOBS:-6}")
BUILT=$IOSEVKA/dist/HariMono/TTF-Unhinted
DONOR=$IOSEVKA/dist/HariMonoDonor/TTF-Unhinted

# 2. Fit symbols, then derive the hinted TTF and WOFF2 from the fitted font.
rm -rf "$OUT" && mkdir -p "$OUT/ttf-unhinted" "$OUT/ttf" "$OUT/woff2" "$OUT/nerd-font"
for style in $STYLES; do
	case $style in
		Bold*) weight=bold; upright=$BUILT/HariMono-Bold.ttf ;;
		SemiBold*) weight=semibold; upright=$BUILT/HariMono-SemiBold.ttf ;;
		Medium*) weight=medium; upright=$BUILT/HariMono-Medium.ttf ;;
		*) weight=regular; upright=$BUILT/HariMono-Regular.ttf ;;
	esac
	case $style in *Italic) slant=$upright ;; *) slant= ;; esac
	fitted=$OUT/ttf-unhinted/HariMono-$style.ttf
	uv run --with fonttools "$HERE/postprocess.py" "$BUILT/HariMono-$style.ttf" "$DONOR/HariMonoDonor-$style.ttf" \
		"$HERE/data/symbol-fit.json" "$weight" "$fitted" $slant
	ttfautohint --no-info "$fitted" "$OUT/ttf/HariMono-$style.ttf"
	uv run --with fonttools --with brotli python -c 'import sys; from fontTools.ttLib import TTFont; f = TTFont(sys.argv[1]); f.flavor = "woff2"; f.save(sys.argv[2])' \
		"$fitted" "$OUT/woff2/HariMono-$style.woff2"
	for f in "$fitted" "$OUT/ttf/HariMono-$style.ttf" "$OUT/woff2/HariMono-$style.woff2"; do ots "$f"; done
done

# 3. Nerd Font version: icons patched into the fitted fonts, every glyph one cell wide.
if [ ! -d "$PATCHER" ]; then
	mkdir -p "$PATCHER"
	curl -sL "https://github.com/ryanoasis/nerd-fonts/releases/download/$NERD_REF/FontPatcher.zip" -o "$PATCHER/FontPatcher.zip"
	(cd "$PATCHER" && unzip -q FontPatcher.zip)
fi
for style in $STYLES; do
	fontforge -quiet -script "$PATCHER/font-patcher" --complete --mono --careful --no-progressbars --quiet \
		--outputdir "$OUT/nerd-font" "$OUT/ttf-unhinted/HariMono-$style.ttf" > /dev/null
done
for f in "$OUT"/nerd-font/*.ttf; do ots "$f"; done

ls -1 "$OUT"/*/
