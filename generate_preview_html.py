preview_html = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>French Noun Gender Cards - Interactive Preview</title>
<style>
/* Global Card Styles */
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  background-color: #EDF2F7;
  margin: 0;
  padding: 30px 15px;
  color: #2D3748;
  display: flex;
  flex-direction: column;
  align-items: center;
}

body.dark {
  background-color: #0F172A;
  color: #E2E8F0;
}

.controls {
  margin-bottom: 25px;
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  justify-content: center;
}

.controls button {
  padding: 10px 18px;
  font-size: 14px;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  background: #3182CE;
  color: #FFFFFF;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: all 0.2s ease;
}

.controls button:hover {
  background: #2B6CB0;
  transform: translateY(-1px);
}

.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  font-size: 18px;
  text-align: center;
  color: #2D3748;
  background-color: transparent;
  margin: 0;
  padding: 10px;
  width: 100%;
}

body.dark .card {
  color: #E2E8F0;
}

/* Main Container */
.card-container {
  max-width: 500px;
  margin: 15px auto;
  padding: 25px;
  background: #FFFFFF;
  border-radius: 16px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  transition: background 0.3s ease;
}

body.dark .card-container {
  background: #2D3748;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5);
}

/* Front Elements */
.instruction {
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: #718096;
  margin-bottom: 20px;
}

.prompt-word {
  font-size: 36px;
  font-weight: 700;
  color: #4A5568;
  margin-bottom: 15px;
}

body.dark .prompt-word {
  color: #EDF2F7;
}

.clue-translation {
  font-size: 15px;
  color: #A0AEC0;
  font-style: italic;
}

/* Back Elements: Dynamic Color Blocks */
.answer-block {
  font-size: 36px;
  font-weight: 800;
  padding: 15px;
  border-radius: 12px;
  margin-bottom: 15px;
  display: inline-block;
  width: 90%;
  box-sizing: border-box;
}

/* Masculine Theme Styling */
.answer-block.Masculine {
  background-color: #EBF8FF;
  color: #2B6CB0;
  border: 2px solid #BEE3F8;
}
body.dark .answer-block.Masculine {
  background-color: #2A4365;
  color: #90CDF4;
  border-color: #2B6CB0;
}

/* Feminine Theme Styling */
.answer-block.Feminine {
  background-color: #FFF5F5;
  color: #C53030;
  border: 2px solid #FED7D7;
}
body.dark .answer-block.Feminine {
  background-color: #653B3B;
  color: #FEB2B2;
  border-color: #9B2C2C;
}

.article {
  text-decoration: underline;
}

/* Divider Line */
#answer-splitter {
  border: 0;
  height: 1px;
  background: #E2E8F0;
  margin: 20px 0;
}
body.dark #answer-splitter {
  background: #4A5568;
}

/* Audio Player */
.audio-player {
  margin: 10px 0 16px 0;
}
.audio-player a {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  background-color: #EDF2F7;
  color: #2D3748;
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  border-radius: 20px;
}
body.dark .audio-player a {
  background-color: #3A4454;
  color: #EDF2F7;
}

/* Metadata Layout */
.metadata-container {
  text-align: left;
  margin-top: 15px;
}

.meta-row {
  display: flex;
  margin-bottom: 12px;
  font-size: 15px;
  line-height: 1.4;
}

.meta-label {
  font-weight: 600;
  min-width: 100px;
  color: #718096;
}
body.dark .meta-label {
  color: #A0AEC0;
}

.meta-value {
  color: #2D3748;
}
body.dark .meta-value {
  color: #E2E8F0;
}

.rule-highlight {
  background-color: #F7FAFC;
  padding: 8px 12px;
  border-radius: 6px;
  border-left: 4px solid #CBD5E0;
}
body.dark .rule-highlight {
  background-color: #3A4454;
  border-left-color: #4A5568;
}

.sentence-block {
  border-top: 1px dashed #E2E8F0;
  padding-top: 10px;
  margin-top: 10px;
}
body.dark .sentence-block {
  border-top-color: #4A5568;
}

.meta-value-italic {
  font-style: italic;
  color: #4A5568;
}
body.dark .meta-value-italic {
  color: #CBD5E0;
}

.demo-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
  gap: 25px;
  width: 100%;
  max-width: 1100px;
}
.card-section-title {
  text-align: center;
  font-size: 14px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 8px;
  color: #718096;
}
body.dark .card-section-title {
  color: #A0AEC0;
}
</style>
</head>
<body>

<div class="controls">
  <button onclick="toggleDarkMode()">🌓 Toggle Dark / Night Mode</button>
</div>

<div class="demo-grid">
  <!-- Card 1: Masculine Pattern (-ment) -->
  <div>
    <div class="card-section-title">Masculine Pattern Card (-ment)</div>
    <div class="card-container">
      <div class="answer-block Masculine">
        <span class="article">un / l'</span> <span class="target-noun">appartement</span>
      </div>
      <hr id="answer-splitter">
      <div class="audio-player">
        <a href="https://translate.google.com/?sl=fr&tl=en&text=un%20appartement&op=translate" target="_blank">🔊 Listen: [un appartement]</a>
      </div>
      <div class="metadata-container">
        <div class="meta-row">
          <span class="meta-label">English:</span>
          <span class="meta-value">apartment / flat</span>
        </div>
        <div class="meta-row rule-highlight">
          <span class="meta-label">Pattern/Rule:</span>
          <span class="meta-value"><strong>-ment</strong> &rarr; Nouns ending in -ment are &gt;99% masculine.</span>
        </div>
        <div class="meta-row sentence-block">
          <span class="meta-label">In Context:</span>
          <span class="meta-value-italic">J'habite dans un bel appartement au centre-ville.</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Card 2: Feminine Pattern (-tion) -->
  <div>
    <div class="card-section-title">Feminine Pattern Card (-tion)</div>
    <div class="card-container">
      <div class="answer-block Feminine">
        <span class="article">une / la</span> <span class="target-noun">situation</span>
      </div>
      <hr id="answer-splitter">
      <div class="audio-player">
        <a href="https://translate.google.com/?sl=fr&tl=en&text=une%20situation&op=translate" target="_blank">🔊 Listen: [une situation]</a>
      </div>
      <div class="metadata-container">
        <div class="meta-row">
          <span class="meta-label">English:</span>
          <span class="meta-value">situation</span>
        </div>
        <div class="meta-row rule-highlight">
          <span class="meta-label">Pattern/Rule:</span>
          <span class="meta-value"><strong>-tion</strong> &rarr; Nouns ending in -tion are &gt;99% feminine (derived from Latin -tio).</span>
        </div>
        <div class="meta-row sentence-block">
          <span class="meta-label">In Context:</span>
          <span class="meta-value-italic">Nous faisons face à une situation tout à fait inédite.</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Card 3: Masculine Exception (musée) -->
  <div>
    <div class="card-section-title">Masculine Exception (-ée Trap)</div>
    <div class="card-container">
      <div class="answer-block Masculine">
        <span class="article">un / le</span> <span class="target-noun">musée</span>
      </div>
      <hr id="answer-splitter">
      <div class="audio-player">
        <a href="https://translate.google.com/?sl=fr&tl=en&text=un%20mus%C3%A9e&op=translate" target="_blank">🔊 Listen: [un musée]</a>
      </div>
      <div class="metadata-container">
        <div class="meta-row">
          <span class="meta-label">English:</span>
          <span class="meta-value">museum</span>
        </div>
        <div class="meta-row rule-highlight">
          <span class="meta-label">Pattern/Rule:</span>
          <span class="meta-value"><strong>Exception: -ée</strong> &rarr; Masculine exception to the feminine -ée ending (from Greek mouseion).</span>
        </div>
        <div class="meta-row sentence-block">
          <span class="meta-label">In Context:</span>
          <span class="meta-value-italic">Le musée du Louvre attire des millions de visiteurs.</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Card 4: Feminine Exception (plage) -->
  <div>
    <div class="card-section-title">Feminine Exception (-age Trap)</div>
    <div class="card-container">
      <div class="answer-block Feminine">
        <span class="article">une / la</span> <span class="target-noun">plage</span>
      </div>
      <hr id="answer-splitter">
      <div class="audio-player">
        <a href="https://translate.google.com/?sl=fr&tl=en&text=une%20plage&op=translate" target="_blank">🔊 Listen: [une plage]</a>
      </div>
      <div class="metadata-container">
        <div class="meta-row">
          <span class="meta-label">English:</span>
          <span class="meta-value">beach</span>
        </div>
        <div class="meta-row rule-highlight">
          <span class="meta-label">Pattern/Rule:</span>
          <span class="meta-value"><strong>Exception: -age</strong> &rarr; Key feminine exception to the masculine -age ending rule.</span>
        </div>
        <div class="meta-row sentence-block">
          <span class="meta-label">In Context:</span>
          <span class="meta-value-italic">Nous posons nos serviettes sur une belle plage de sable fin.</span>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
function toggleDarkMode() {
  document.body.classList.toggle('dark');
}
</script>

</body>
</html>
"""

with open("French_Noun_Gender_Preview.html", "w", encoding="utf-8") as f:
    f.write(preview_html)

print("Generated French_Noun_Gender_Preview.html")
