import shutil
from pathlib import Path
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parent.parent
assets = root / "assets"
pictures = Path("/Users/vimalhari/Pictures")
brain_dir = Path("/Users/vimalhari/.gemini/antigravity-cli/brain/d0e9eac5-6610-4835-a6d9-d5199ee21444")

def make_html(theme: str) -> str:
    if theme == "amber":
        bg_color = "#0c0905"
        bg_images = """
            radial-gradient(circle at 14% 15%, rgba(255, 160, 0, 0.16) 0%, transparent 42%),
            radial-gradient(circle at 86% 22%, rgba(255, 120, 0, 0.12) 0%, transparent 45%),
            radial-gradient(circle at 50% 85%, rgba(255, 180, 50, 0.08) 0%, transparent 48%),
            radial-gradient(circle, rgba(255, 176, 0, 0.06) 1px, transparent 1px)
        """
        text_color = "#fbe7c6"
        card_bg = "rgba(20, 15, 9, 0.94)"
        card_border = "rgba(255, 176, 0, 0.18)"
        card_shadow = "0 16px 44px rgba(0, 0, 0, 0.75)"
        win_header = "rgba(30, 22, 13, 0.96)"
        active_tab = "#332211"
        line_num = "#7a5a3a"
        term_bg = "#070503"
        prompt_col = "#ffb74d"
        box_table_col = "#ffb000"
        sub_col = "#b09575"
        meta_note_col = "#9e8060"
        feat_bg = "rgba(26, 19, 11, 0.95)"
        glyph_desc_col = "#baa082"
        badge_bg = "rgba(255, 160, 0, 0.18)"
        badge_col = "#ffb000"
        badge_border = "rgba(255, 160, 0, 0.4)"
        badge2_bg = "rgba(255, 183, 77, 0.15)"
        badge2_col = "#ffb74d"
        badge2_border = "rgba(255, 183, 77, 0.35)"
        badge3_bg = "rgba(255, 204, 128, 0.15)"
        badge3_col = "#ffcc80"
        badge3_border = "rgba(255, 204, 128, 0.35)"
        k_col = "#ff8a65"
        s_col = "#ffd54f"
        c_col = "#a1887f"
        f_col = "#ffe082"
        n_col = "#ffb74d"
        t_col = "#ffab91"
        p_col = "#ffe082"
        stat_val_col = "#ffe082"
        accent_col = "#ffb000"
        cyan_col = "#ffe082"
        green_col = "#ffca28"
        purple_col = "#ffab91"
        alpha_col = "#f5d7b0"
    elif theme == "light":
        bg_color = "#f4f6f8"
        bg_images = """
            radial-gradient(circle at 14% 15%, rgba(230, 122, 44, 0.08) 0%, transparent 40%),
            radial-gradient(circle at 86% 22%, rgba(9, 105, 218, 0.06) 0%, transparent 42%),
            radial-gradient(circle at 50% 85%, rgba(130, 80, 223, 0.05) 0%, transparent 45%),
            radial-gradient(circle, rgba(0, 0, 0, 0.05) 1px, transparent 1px)
        """
        text_color = "#1f2328"
        card_bg = "rgba(255, 255, 255, 0.94)"
        card_border = "rgba(0, 0, 0, 0.10)"
        card_shadow = "0 16px 40px rgba(0, 0, 0, 0.08)"
        win_header = "rgba(246, 248, 250, 0.98)"
        active_tab = "#ffffff"
        line_num = "#8c959f"
        term_bg = "#1f2328"
        prompt_col = "#79c0ff"
        box_table_col = "#58a6ff"
        sub_col = "#57606a"
        meta_note_col = "#6e7781"
        feat_bg = "rgba(255, 255, 255, 0.98)"
        glyph_desc_col = "#57606a"
        badge_bg = "rgba(230, 122, 44, 0.12)"
        badge_col = "#cf5a0e"
        badge_border = "rgba(230, 122, 44, 0.3)"
        badge2_bg = "rgba(9, 105, 218, 0.10)"
        badge2_col = "#0969da"
        badge2_border = "rgba(9, 105, 218, 0.25)"
        badge3_bg = "rgba(26, 127, 55, 0.10)"
        badge3_col = "#1a7f37"
        badge3_border = "rgba(26, 127, 55, 0.25)"
        k_col = "#cf222e"
        s_col = "#0a3069"
        c_col = "#6e7781"
        f_col = "#8250df"
        n_col = "#0969da"
        t_col = "#953800"
        p_col = "#116329"
        stat_val_col = "#3fb950"
        accent_col = "#cf5a0e"
        cyan_col = "#0969da"
        green_col = "#1a7f37"
        purple_col = "#8250df"
        alpha_col = "#24292f"
    else: # obsidian dark
        bg_color = "#07090e"
        bg_images = """
            radial-gradient(circle at 14% 15%, rgba(230, 122, 44, 0.12) 0%, transparent 42%),
            radial-gradient(circle at 86% 22%, rgba(56, 189, 248, 0.09) 0%, transparent 45%),
            radial-gradient(circle at 50% 85%, rgba(168, 85, 247, 0.07) 0%, transparent 48%),
            radial-gradient(circle, rgba(255, 255, 255, 0.045) 1px, transparent 1px)
        """
        text_color = "#e6edf3"
        card_bg = "rgba(12, 16, 22, 0.94)"
        card_border = "rgba(255, 255, 255, 0.08)"
        card_shadow = "0 16px 44px rgba(0, 0, 0, 0.6)"
        win_header = "rgba(18, 23, 31, 0.96)"
        active_tab = "#1f2633"
        line_num = "#484f58"
        term_bg = "#080a0f"
        prompt_col = "#58a6ff"
        box_table_col = "#79c0ff"
        sub_col = "#8b949e"
        meta_note_col = "#8b949e"
        feat_bg = "rgba(16, 20, 27, 0.95)"
        glyph_desc_col = "#8b949e"
        badge_bg = "rgba(230, 122, 44, 0.15)"
        badge_col = "#ff9e3b"
        badge_border = "rgba(230, 122, 44, 0.35)"
        badge2_bg = "rgba(56, 189, 248, 0.12)"
        badge2_col = "#38bdf8"
        badge2_border = "rgba(56, 189, 248, 0.3)"
        badge3_bg = "rgba(126, 231, 135, 0.12)"
        badge3_col = "#7ee787"
        badge3_border = "rgba(126, 231, 135, 0.3)"
        k_col = "#ff7b72"
        s_col = "#a5d6a7"
        c_col = "#8b949e"
        f_col = "#d2a8ff"
        n_col = "#79c0ff"
        t_col = "#ffa657"
        p_col = "#ffc66d"
        stat_val_col = "#7ee787"
        accent_col = "#ff9e3b"
        cyan_col = "#38bdf8"
        green_col = "#7ee787"
        purple_col = "#d2a8ff"
        alpha_col = "#c9d1d9"

    term_text_style = "color: #e6edf3;" if theme == "light" else f"color: {text_color};"

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Hari Mono Specimen ({theme.title()})</title>
<style>
@font-face {{
  font-family: 'Hari Mono';
  src: url('../dist/ttf-unhinted/HariMono-Regular.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
}}
@font-face {{
  font-family: 'Hari Mono';
  src: url('../dist/ttf-unhinted/HariMono-Bold.ttf') format('truetype');
  font-weight: 700;
  font-style: normal;
}}
@font-face {{
  font-family: 'Hari Mono';
  src: url('../dist/ttf-unhinted/HariMono-Italic.ttf') format('truetype');
  font-weight: 400;
  font-style: italic;
}}
@font-face {{
  font-family: 'Hari Mono';
  src: url('../dist/ttf-unhinted/HariMono-BoldItalic.ttf') format('truetype');
  font-weight: 700;
  font-style: italic;
}}

* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}

body {{
  background-color: {bg_color};
  background-image: {bg_images};
  background-size: auto, auto, auto, 24px 24px;
  color: {text_color};
  font-family: 'Hari Mono', monospace;
  width: 2560px;
  height: 1440px;
  padding: 48px 64px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow: hidden;
  -webkit-font-smoothing: antialiased;
}}

.header {{
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  border-bottom: 1px solid rgba(127, 127, 127, 0.18);
  padding-bottom: 24px;
}}

.title-wrap {{
  display: flex;
  flex-direction: column;
  gap: 10px;
}}

.badge-row {{
  display: flex;
  align-items: center;
  gap: 10px;
}}

.badge {{
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 4px 10px;
  border-radius: 6px;
  background: {badge_bg};
  color: {badge_col};
  border: 1px solid {badge_border};
}}

.badge-second {{
  background: {badge2_bg};
  color: {badge2_col};
  border: 1px solid {badge2_border};
}}

.badge-third {{
  background: {badge3_bg};
  color: {badge3_col};
  border: 1px solid {badge3_border};
}}

h1 {{
  font-size: 76px;
  font-weight: 700;
  letter-spacing: -2px;
  color: {text_color};
  line-height: 1;
}}

.subtitle {{
  font-size: 20px;
  color: {sub_col};
  letter-spacing: 0.2px;
}}

.header-meta {{
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 8px;
  text-align: right;
}}

.meta-spec {{
  font-size: 16px;
  color: {text_color};
}}

.meta-spec b {{
  color: {badge_col};
}}

.meta-note {{
  font-size: 14px;
  color: {meta_note_col};
}}

.main-grid {{
  display: grid;
  grid-template-columns: 1460px 1fr;
  gap: 36px;
  flex: 1;
  margin: 24px 0;
}}

.left-col {{
  display: flex;
  flex-direction: column;
  gap: 20px;
}}

.card {{
  background: {card_bg};
  border: 1px solid {card_border};
  border-radius: 12px;
  box-shadow: {card_shadow};
  overflow: hidden;
  backdrop-filter: blur(20px);
}}

.window-header {{
  background: {win_header};
  border-bottom: 1px solid rgba(127, 127, 127, 0.12);
  padding: 11px 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}}

.traffic-lights {{
  display: flex;
  gap: 8px;
  align-items: center;
}}

.dot {{
  width: 12px;
  height: 12px;
  border-radius: 50%;
}}

.dot-red {{ background: #ff5f56; }}
.dot-yellow {{ background: #ffbd2e; }}
.dot-green {{ background: #27c93f; }}

.tab-bar {{
  display: flex;
  gap: 4px;
}}

.tab {{
  font-size: 13px;
  padding: 5px 14px;
  border-radius: 6px;
  color: {sub_col};
}}

.tab.active {{
  background: {active_tab};
  color: {text_color};
  font-weight: 700;
  border: 1px solid rgba(127, 127, 127, 0.15);
}}

.window-title {{
  font-size: 13px;
  color: {sub_col};
}}

.editor-wrap {{
  display: flex;
  padding: 20px 22px;
  font-size: 15.5px;
  line-height: 1.62;
}}

.line-numbers {{
  color: {line_num};
  user-select: none;
  padding-right: 20px;
  text-align: right;
  border-right: 1px solid rgba(127, 127, 127, 0.12);
  font-size: 14.5px;
}}

.code-content {{
  padding-left: 22px;
  flex: 1;
  overflow: hidden;
}}

pre {{
  font-family: 'Hari Mono', monospace;
}}

.k {{ color: {k_col}; font-weight: 700; }}
.s {{ color: {s_col}; }}
.c {{ color: {c_col}; font-style: italic; }}
.f {{ color: {f_col}; font-weight: 700; }}
.n {{ color: {n_col}; }}
.t {{ color: {t_col}; }}
.p {{ color: {p_col}; }}
.op {{ color: {text_color}; }}

.terminal-body {{
  padding: 18px 24px;
  font-size: 14.5px;
  line-height: 1.48;
  background: {term_bg};
  {term_text_style}
}}

.prompt {{
  color: {prompt_col};
  margin-bottom: 10px;
  font-size: 14.5px;
}}

.prompt-cmd {{
  color: #f0f6fc;
}}

.box-table {{
  color: {box_table_col};
  line-height: 1.25;
  margin: 6px 0;
  font-size: 14px;
}}

.term-stat {{
  margin-top: 10px;
  display: flex;
  gap: 28px;
  color: #8b949e;
  font-size: 13px;
}}

.stat-val {{
  color: {stat_val_col};
  font-weight: 700;
}}

.right-col {{
  display: flex;
  flex-direction: column;
  gap: 18px;
}}

.lab-title {{
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1.2px;
  color: {sub_col};
  display: flex;
  align-items: center;
  gap: 8px;
}}

.lab-title::before {{
  content: '';
  display: inline-block;
  width: 8px;
  height: 8px;
  background: {badge_col};
  border-radius: 2px;
}}

.feature-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}}

.feature-box {{
  background: {feat_bg};
  border: 1px solid {card_border};
  border-radius: 10px;
  padding: 16px 18px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}}

.glyph-showcase {{
  font-size: 46px;
  font-weight: 700;
  line-height: 1;
  color: {text_color};
  display: flex;
  align-items: baseline;
  gap: 12px;
}}

.accent {{ color: {accent_col}; }}
.cyan {{ color: {cyan_col}; }}
.green {{ color: {green_col}; }}
.purple {{ color: {purple_col}; }}

.glyph-label {{
  font-size: 13.5px;
  font-weight: 700;
  color: {text_color};
}}

.glyph-desc {{
  font-size: 12px;
  color: {glyph_desc_col};
  line-height: 1.42;
}}

.weights-box {{
  background: {feat_bg};
  border: 1px solid {card_border};
  border-radius: 10px;
  padding: 16px 20px;
  display: flex;
  flex-direction: column;
  gap: 9px;
}}

.weight-row {{
  display: flex;
  align-items: baseline;
  font-size: 14.5px;
  border-bottom: 1px solid rgba(127, 127, 127, 0.1);
  padding-bottom: 6px;
  gap: 14px;
}}

.weight-row:last-child {{
  border-bottom: none;
  padding-bottom: 0;
}}

.weight-tag {{
  font-size: 11.5px;
  color: {badge_col};
  text-transform: uppercase;
  letter-spacing: 0.6px;
  min-width: 105px;
  font-weight: 700;
}}

.weight-sample {{
  color: {text_color};
  flex: 1;
}}

.symbols-box {{
  background: {feat_bg};
  border: 1px solid {card_border};
  border-radius: 10px;
  padding: 15px 20px;
  display: flex;
  flex-direction: column;
  gap: 7px;
}}

.symbols-grid {{
  font-size: 18.5px;
  line-height: 1.45;
  color: {cyan_col};
  letter-spacing: 2px;
}}

.alphabet-box {{
  background: {feat_bg};
  border: 1px solid {card_border};
  border-radius: 10px;
  padding: 14px 20px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}}

.alpha-line {{
  font-size: 13.5px;
  color: {alpha_col};
  letter-spacing: 1.8px;
}}

.footer {{
  border-top: 1px solid rgba(127, 127, 127, 0.18);
  padding-top: 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 14px;
  color: {sub_col};
}}

.footer-left {{
  display: flex;
  gap: 22px;
}}

.footer-right {{
  color: {badge_col};
  font-weight: 700;
}}
</style>
</head>
<body>

  <div class="header">
    <div class="title-wrap">
      <div class="badge-row">
        <span class="badge">Hari Mono Typeface</span>
        <span class="badge badge-second">600 FUnit Pitch</span>
        <span class="badge badge-third">Pure WYSIWYG Code</span>
      </div>
      <h1>Hari Mono</h1>
      <div class="subtitle">A spatial-efficient monospace font family engineered for programming and technical prose.</div>
    </div>
    <div class="header-meta">
      <div class="meta-spec">Built with <b>Iosevka</b> in the spirit of <b>Berkeley Mono</b></div>
      <div class="meta-note">Version 1.0.1 (2026) : Designed and authored by Vimal Hari</div>
    </div>
  </div>

  <div class="main-grid">

    <div class="left-col">

      <div class="card">
        <div class="window-header">
          <div class="traffic-lights">
            <div class="dot dot-red"></div>
            <div class="dot dot-yellow"></div>
            <div class="dot dot-green"></div>
          </div>
          <div class="tab-bar">
            <div class="tab active">stream_engine.rs</div>
            <div class="tab">telemetry.rs</div>
            <div class="tab">config.toml</div>
          </div>
          <div class="window-title">Hari Mono Regular 15.5px : Rust Editor Buffer</div>
        </div>
        <div class="editor-wrap">
          <div class="line-numbers">
01<br>02<br>03<br>04<br>05<br>06<br>07<br>08<br>09<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19
          </div>
          <div class="code-content">
<pre><span class="c">// Spatial efficiency: 600 units per cell preserves geometric rhythm across deep nesting</span>
<span class="k">pub async fn</span> <span class="f">process_telemetry_batch</span>&lt;<span class="t">'a</span>, <span class="t">T</span>&gt;(
    <span class="p">buffer</span>: <span class="op">&amp;</span><span class="t">'a mut</span> <span class="t">StreamBuffer</span>&lt;<span class="t">T</span>, <span class="n">600</span>&gt;,
    <span class="p">threshold</span>: <span class="t">f64</span>,
) -&gt; <span class="t">Result</span>&lt;<span class="t">BatchSummary</span>, <span class="t">EngineError</span>&gt; 
<span class="k">where</span>
    <span class="t">T</span>: <span class="t">TelemetryEvent</span> + <span class="t">Send</span> + <span class="t">Sync</span>,
{{
    <span class="k">let</span> <span class="p">valid_entries</span> = buffer.filter(|<span class="p">e</span>| e.latency_ms &lt;= threshold &amp;&amp; e.status !== <span class="n">500</span>);
    <span class="k">let</span> <span class="p">sample_id</span>: <span class="t">u64</span> = <span class="n">0x7F00_10A3</span>; <span class="c">// Dotted zero: 0 vs O disambiguation</span>

    <span class="k">match</span> buffer.flush_pipeline(<span class="n">32</span>, <span class="p">sample_id</span>).<span class="k">await</span> {{
        <span class="t">Ok</span>(<span class="p">stats</span>) <span class="k">if</span> stats.processed &gt;= <span class="n">10_000</span> =&gt; {{
            <span class="k">let</span> <span class="p">q</span> = (<span class="p">stats</span>.ratio * <span class="n">100.0</span>).round() <span class="k">as</span> <span class="t">u32</span>; <span class="c">// Flat-topped 3</span>
            <span class="t">Ok</span>(<span class="t">BatchSummary</span> {{ total: stats.processed, health_score: q, active: <span class="k">true</span> }})
        }}
        <span class="t">Ok</span>(<span class="p">stats</span>) =&gt; <span class="t">Ok</span>(<span class="t">BatchSummary</span>::from_partial(stats)),
        <span class="t">Err</span>(<span class="p">err</span>) =&gt; <span class="t">Err</span>(<span class="t">EngineError</span>::PipelineFault(err)),
    }}
}}
</pre>
          </div>
        </div>
      </div>

      <div class="card">
        <div class="window-header">
          <div class="traffic-lights">
            <div class="dot dot-red"></div>
            <div class="dot dot-yellow"></div>
            <div class="dot dot-green"></div>
          </div>
          <div class="window-title">ghostty : 108x16 : zsh : Hari Mono 14.5px</div>
          <div class="window-title" style="color: {stat_val_col};">● session active</div>
        </div>
        <div class="terminal-body">
          <div class="prompt">vimal@zorinto ➜ ~/hari-mono [git:main] ❯ <span class="prompt-cmd">cargo bench --bench character_matrix</span></div>
          <pre class="box-table">┌─────────────────────────────┬──────────────┬─────────────┬────────────┐
│ BENCHMARK METRIC            │ MEASUREMENT  │ LATENCY p99 │ CELL FIT   │
├─────────────────────────────┼──────────────┼─────────────┼────────────┤
│ Cell geometry validation    │  600.00 UPM  │    0.04 ms  │  UNIFORM   │
│ Disambiguation quartet      │ 100% distinct│    0.08 ms  │  OPTIMAL   │
│ Box drawing alignment       │  Seamless    │    0.02 ms  │  PERFECT   │
│ Symbol stroke weight fit    │  17 symbols  │    0.11 ms  │  BALANCED  │
└─────────────────────────────┴──────────────┴─────────────┴────────────┘</pre>
          <div class="term-stat">
            <div>TEST SUITE: <span class="stat-val">34 PASSED</span></div>
            <div>STYLES: <span class="stat-val">4 ACTIVE</span></div>
            <div>NERD FONTS: <span class="stat-val">10,000+ ICONS</span></div>
            <div>LIGATURES: <span class="stat-val">STRICT OFF (PURE WYSIWYG)</span></div>
          </div>
        </div>
      </div>

    </div>

    <div class="right-col">

      <div class="lab-title">Typographic Anatomy and Disambiguation</div>

      <div class="feature-grid">

        <div class="feature-box">
          <div class="glyph-showcase">
            <span class="accent">0</span> <span style="font-size:24px; color:{sub_col};">vs</span> <span class="cyan">O</span>
          </div>
          <div class="glyph-label">Dotted Zero Disambiguation</div>
          <div class="glyph-desc">Clean internal dot prevents critical bugs between numeric 0 and capital letter O.</div>
        </div>

        <div class="feature-box">
          <div class="glyph-showcase">
            <span class="accent">1</span> <span class="cyan">l</span> <span class="green">I</span> <span class="purple">|</span>
          </div>
          <div class="glyph-label">Disambiguation Quartet</div>
          <div class="glyph-desc">Distinct top serif on 1, curved bottom hook on l, serifs on I, and tall pipe |.</div>
        </div>

        <div class="feature-box">
          <div class="glyph-showcase">
            <span class="accent">g</span> <span style="font-size:24px; color:{sub_col};">&amp;</span> <span class="cyan">3</span>
          </div>
          <div class="glyph-label">Single-Storey g and Flat 3</div>
          <div class="glyph-desc">Open bowl g provides immediate legibility; flat-topped 3 gives architectural precision.</div>
        </div>

        <div class="feature-box">
          <div class="glyph-showcase" style="font-size:32px;">
            <span class="accent">!==</span> <span class="cyan">=&gt;</span> <span class="green">-&gt;</span>
          </div>
          <div class="glyph-label">Strict WYSIWYG Operators</div>
          <div class="glyph-desc">No ligatures. Arrows and equality operators stay as typed for true code fidelity.</div>
        </div>

      </div>

      <div class="weights-box">
        <div class="lab-title" style="margin-bottom:4px;">Family Weights and Slopes</div>

        <div class="weight-row">
          <div class="weight-tag">Regular</div>
          <div class="weight-sample" style="font-weight:400; font-style:normal;">
            The quick brown fox jumps over the lazy dog. 0123456789
          </div>
        </div>

        <div class="weight-row">
          <div class="weight-tag">Bold</div>
          <div class="weight-sample" style="font-weight:700; font-style:normal;">
            Sphinx of black quartz, judge my vow. ABCDEFGHIJKLMNOPQRSTUVWXYZ
          </div>
        </div>

        <div class="weight-row">
          <div class="weight-tag">Italic</div>
          <div class="weight-sample" style="font-weight:400; font-style:italic;">
            Slanted letterforms preserve identical character width and reading cadence.
          </div>
        </div>

        <div class="weight-row">
          <div class="weight-tag">Bold Italic</div>
          <div class="weight-sample" style="font-weight:700; font-style:italic;">
            High-contrast visual emphasis in terminal prompts and headers.
          </div>
        </div>
      </div>

      <div class="symbols-box">
        <div class="lab-title" style="margin-bottom:4px;">Symbol Fit and Mathematical Palette</div>
        <div class="symbols-grid">
          λ π ∑ ∫ √ ≈ ≠ ≤ ≥ ± ∞ ∂ ∆ ∇ µ α β γ ⊕ ⊗ ∩ ∪ ∈ ∉ ⊂ ⊃
        </div>
        <div class="symbols-grid" style="color: {accent_col}; font-size: 16.5px; margin-top: 3px;">
          ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼ │ ─ ═ ║ ▲ ▼ ◀ ▶ ░ ▒ ▓ █ ◆ ● £ $ € ¥ ₹ ¢ ₿
        </div>
        <div class="symbols-grid" style="color: {sub_col}; font-size: 15.5px; margin-top: 2px;">
          () [] {{}} &lt;&gt; ` ~ ^ _ @ # % &amp; * / \ | ! ? ; : " '
        </div>
      </div>

      <div class="alphabet-box">
        <div class="lab-title" style="margin-bottom:4px;">Character Set Cascade</div>
        <div class="alpha-line">ABCDEFGHIJKLMNOPQRSTUVWXYZ</div>
        <div class="alpha-line" style="color: {sub_col};">abcdefghijklmnopqrstuvwxyz</div>
        <div class="alpha-line" style="color: {accent_col};">0123456789 0O 1lI| {{}}[]() &lt;=&gt; ~^`_</div>
      </div>

    </div>

  </div>

  <div class="footer">
    <div class="footer-left">
      <div><b>Typeface:</b> Hari Mono</div>
      <div><b>Format:</b> TrueType (Hinted and Unhinted), WOFF2, Nerd Font</div>
      <div><b>Spacing:</b> Monospaced (600 FUnit cell)</div>
      <div><b>Licence:</b> SIL Open Font License 1.1</div>
    </div>
    <div class="footer-right">
      github.com/zorinto/hari-mono
    </div>
  </div>

</body>
</html>
"""

themes = ["dark", "amber", "light"]

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        headless=True
    )
    
    for theme in themes:
        html = make_html(theme)
        suffix = "" if theme == "dark" else f"-{theme}"
        html_file = assets / f"specimen_poster{suffix}.html"
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html)
        
        img_name = f"hari-mono-showcase{suffix}.png"
        img_retina = f"hari-mono-showcase{suffix}-retina.png"
        
        target_png = assets / img_name
        target_retina = assets / img_retina
        
        page = browser.new_page(viewport={"width": 2560, "height": 1440}, device_scale_factor=1)
        page.goto(f"file://{html_file}")
        page.wait_for_load_state("networkidle")
        page.screenshot(path=str(target_png))
        
        page_ret = browser.new_page(viewport={"width": 2560, "height": 1440}, device_scale_factor=2)
        page_ret.goto(f"file://{html_file}")
        page_ret.wait_for_load_state("networkidle")
        page_ret.screenshot(path=str(target_retina))
        
        print(f"Generated {img_name} and {img_retina}")
        
        # Copy to Pictures folder
        if pictures.exists():
            shutil.copy2(target_png, pictures / img_name)
            shutil.copy2(target_retina, pictures / img_retina)
            
        # Copy to brain artifact directory
        if brain_dir.exists():
            shutil.copy2(target_png, brain_dir / img_name)
            shutil.copy2(target_retina, brain_dir / img_retina)

    browser.close()

# Update assets/specimen.png with the new dark showcase
shutil.copy2(assets / "hari-mono-showcase.png", assets / "specimen.png")
print("Updated assets/specimen.png successfully!")
