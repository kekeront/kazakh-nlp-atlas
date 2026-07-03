import { PAPERS } from "@/lib/data";

export function Footer() {
  return (
    <footer>
      <h4>Как построен этот атлас</h4>
      <p>
        Корпус из {PAPERS.length} работ собран скриптом <code>scrape_papers.py</code> из двух
        источников: arXiv API и Semantic Scholar Graph API. Scope — только казахский язык
        (фильтр: упоминание Kazakh/Qazaq + NLP/ML-релевантность). Рёбра графа — реальные цитаты,
        вытянутые через S2 batch (<code>scrape_citations.py</code>). Редакторский слой (флагманы,
        незанятые земли, линия прорывов) — ручная верификация по первоисточникам.
      </p>
      <p className="cav">
        ⚠ Ограничения честно: Semantic Scholar частично отдавал HTTP 429 — non-arXiv покрытие в
        категориях tokenization/LLM/morphology неполное. Авто-тэги — эвристика по абстракту, не
        ручная разметка. Столбец «claim» у флагманов отражает заявления авторов, не проверенную
        истину. Скрейперы идемпотентны — дозапуск пополнит корпус.
      </p>
      <p>
        Источники:{" "}
        <a href="http://export.arxiv.org/api/query" target="_blank" rel="noopener noreferrer">arXiv API</a> ·{" "}
        <a href="https://api.semanticscholar.org" target="_blank" rel="noopener noreferrer">Semantic Scholar</a> ·
        gold-стандарт морфологии:{" "}
        <a href="https://github.com/UniversalDependencies/UD_Kazakh-KTB" target="_blank" rel="noopener noreferrer">UD_Kazakh-KTB</a>,{" "}
        <a href="https://wiki.apertium.org/wiki/Apertium-kaz" target="_blank" rel="noopener noreferrer">apertium-kaz</a>.
      </p>
    </footer>
  );
}
