# EasyBack UI Design Notes

## Buttons

All `QPushButton`s in the app — main-menu buttons and the popup side/helper
buttons — share one look and one layout convention.

### Look

Buttons are rounded and dark. Their visual style comes from the **window
stylesheet's `QPushButton` rule**, not from per-button styling:

- `all_styles.py` `SETTINGS_MAIN` — for the popups (AI Settings, etc.)
- an inline `*{ ... }` sheet in `d_MainWindow.py` — for the main window

Key properties: `border: 2px solid; border-color: rgb(110,110,110);
border-radius: 15px` (20px in the main window); `background-color:
rgba(60,60,60,80)`; `color: rgb(230,230,230)`; plus `:hover` (blue `#2B79C2`)
and `:pressed` states.

Do **not** restyle a button's border/background individually — let the window
sheet provide them.

### Icon left, text right

The icon is pinned to the left edge and the label is right-aligned, with a wide
gap between them. Qt draws a button's icon and text as a single left-aligned
block, so the text cannot simply be right-aligned via the stylesheet without
moving the icon too. The convention instead:

1. **Per-button stylesheet:** `text-align: left; padding-left: 10px;
   padding-right: 2px;` — small left indent (icon near the left border) and a
   nearly-flush right padding (label almost touches the right border).

2. **Space-pad the label** to push it to the right. The label is prefixed with
   however many spaces fill the gap between the icon and the right padding,
   measured with the button's own font. The constants must match the stylesheet
   padding:

   ```python
   pad_left, pad_right, border, icon_gap = 10, 2, 2, 4
   target_right = btn.maximumWidth() - border - pad_right
   text_start   = border + pad_left + btn.iconSize().width() + icon_gap
   gap          = target_right - text_start - fm.horizontalAdvance(text)
   btn.setText(" " * max(0, int(gap / space_w)) + text)
   ```

   See `_align_texts_right` (`d_MainWindow.py`) and `_align_side_texts_right`
   (`d__ai_settings.py`).

3. **Use `int()` (floor), not `round()`,** for the space count. Short labels
   need many filler spaces, and `round()` lets the per-space measurement error
   accumulate and push the label a few pixels past the right border. `int()`
   guarantees the label never overshoots (it lands at most one space short).

### Critical gotcha: set the font explicitly

Call `setFont()` on every button with the rendered font — `QFont` family
`"Lexend Light"`, 16pt, not bold/italic — **before** running the alignment.
`QFontMetrics(btn.font())` must measure the *same* font that renders; otherwise
it measures the tiny default app font, the space padding massively overshoots,
and the label flies off the right edge.

### Icon size depends on the icon's shape

The icon box width feeds the alignment math (`iconSize().width()`), so pick it
per icon shape:

- **Tall, narrow strip icons** (e.g. the select/deselect checkbox-column SVGs,
  viewBox ~12×54): use a tall narrow box `QSize(24, 48)` so they render as a
  full-height strip.
- **Normal square-ish icons** (gear, etc.): use a square-ish box ~`QSize(40, 40)`
  to `QSize(46, 46)` (main-menu buttons use 46×46). A square icon forced into
  the 24×48 strip box renders tiny.

### Sizing and column alignment

Buttons get fixed `setMinimumSize`/`setMaximumSize`; the standard menu/side
button width is 210px. To align a button column with another row, build both as
equal-width pixel blocks centred by matching expanding `QSpacerItem`s with the
same explicit layout `setSpacing`. Example (AI Settings): the list row is
`530 + 10 gap + 210 column = 750`, matching the bottom button row
(`FindLLM 140 + Backup 120 + Export 120 + Import 120 + MainMenu 210` with 10px
gaps), so the list's right edge meets Import and the side buttons align under
Main Menu.

### Where the side-button icons live

The AI Settings select/deselect SVGs are in `ui/icons/` and are loaded by
absolute path (`_side_icon`), **not** from the compiled Qt resource
(`dop_win_rc`).
