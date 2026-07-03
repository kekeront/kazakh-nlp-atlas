// Curated editorial layer — hand-verified from primary sources (June 2026).
// Ported from the Python prototype (build_map.py). This is the analysis that
// turns a pile of scraped papers into an argument.

import type { CategoryMeta, FlagshipModel, Gap, Milestone } from "./types";

export const CATEGORY_META: Record<string, CategoryMeta> = {
  "language-model": { label: "Языковые модели / LLM", icon: "◈" },
  tokenization: {
    label: "Токенизация",
    icon: "◇",
    frontier:
      "Тонкая граница. Почти всё — за 2024–2026. Независимого аудита морфем-выравнивания нет.",
  },
  morphology: {
    label: "Морфология / сегментация",
    icon: "❖",
    frontier:
      "Строят новые сегментаторы, но не аудируют, что делают существующие токенайзеры.",
  },
  "machine-translation": { label: "Машинный перевод", icon: "⇄" },
  speech: { label: "Речь (ASR / TTS)", icon: "◉" },
  "ner-ie": { label: "NER / извлечение", icon: "◎" },
  "dataset-corpus": { label: "Датасеты / корпуса", icon: "▤" },
  evaluation: {
    label: "Оценка / бенчмарки",
    icon: "▣",
    frontier:
      "Бенчмарков мало, и они разрозненны. Til-Core вышел с НУЛЁМ опубликованных метрик.",
  },
  classification: { label: "Классификация / сентимент", icon: "◐" },
  embeddings: { label: "Эмбеддинги", icon: "✶" },
  other: { label: "Прочее", icon: "·" },
};

export const CATEGORY_ORDER: string[] = [
  "tokenization", "morphology", "language-model", "evaluation",
  "embeddings", "classification", "ner-ie", "machine-translation",
  "speech", "dataset-corpus", "other",
];

export const CATEGORY_COLORS: Record<string, string> = {
  tokenization: "#e08a4a", morphology: "#f0a35a", "language-model": "#e9b949",
  evaluation: "#d4b483", "machine-translation": "#54b9d8", speech: "#4a90b8",
  "ner-ie": "#6fc0a8", "dataset-corpus": "#7d9bc4", classification: "#b88fc0",
  embeddings: "#8fbf9f", other: "#6f7d82", global: "#f8d986",
};

export const THESIS =
  "Казахский NLP пережил взрыв в 2024–2026 — но рост сконцентрирован в речи и " +
  "машинном переводе. Токенизация и морфология остаются тонкой, недокартированной " +
  "границей. Именно там открыты контрибьюшены.";

export const MILESTONES: Milestone[] = [
  { year: 2013, scope: "global", label: "word2vec", what: "Плотные векторные представления слов.", url: "https://arxiv.org/abs/1301.3781" },
  { year: 2014, scope: "global", label: "seq2seq", what: "Encoder-decoder: перевод как генерация.", url: "https://arxiv.org/abs/1409.3215" },
  { year: 2014, scope: "global", label: "Attention (Bahdanau)", what: "Выравнивание — конец bottleneck'а.", url: "https://arxiv.org/abs/1409.0473" },
  { year: 2016, scope: "global", label: "BPE для NMT (Sennrich)", what: "Subword-юниты → редкие слова и морфология становятся подъёмны.", url: "https://arxiv.org/abs/1508.07909" },
  { year: 2017, scope: "global", label: "Transformer", what: "«Attention is All You Need» — архитектура всей эпохи.", url: "https://arxiv.org/abs/1706.03762" },
  { year: 2018, scope: "global", label: "BERT", what: "Двунаправленный pretraining, перенос на задачи.", url: "https://arxiv.org/abs/1810.04805" },
  { year: 2019, scope: "kazakh", label: "Первые continuous ASR / NMT", what: "Казахская речь и перевод заходят в нейросети.", url: null },
  { year: 2019, scope: "global", label: "XLM-R", what: "Мультиязычный pretraining на 100 языках — казахский внутри.", url: "https://arxiv.org/abs/1911.02116" },
  { year: 2020, scope: "kazakh", label: "Kazakh Speech Corpus (KSC)", what: "Фундаментальный датасет — хаб №1 в графе цитирований.", url: "https://arxiv.org/abs/2009.10334" },
  { year: 2020, scope: "global", label: "GPT-3", what: "In-context learning: масштаб как способность.", url: "https://arxiv.org/abs/2005.14165" },
  { year: 2021, scope: "kazakh", label: "KazNERD + KazakhTTS", what: "Первые открытые NER и TTS ресурсы для казахского.", url: "https://arxiv.org/abs/2111.13419" },
  { year: 2021, scope: "global", label: "How Good is Your Tokenizer", what: "Fertility: цена токенайзера для не-английского.", url: "https://arxiv.org/abs/2012.15613" },
  { year: 2022, scope: "kazakh", label: "KazRoBERTa", what: "Первая казахская предобученная языковая модель (BPE 32k).", url: null },
  { year: 2022, scope: "global", label: "Chinchilla", what: "Compute-optimal: данных важнее, чем размера.", url: "https://arxiv.org/abs/2203.15556" },
  { year: 2023, scope: "global", label: "LLaMA + Tokenizer Unfairness", what: "Открытые веса → волна локальных адаптаций; токен-налог low-resource измерен.", url: "https://arxiv.org/abs/2305.15425" },
  { year: 2024, scope: "kazakh", label: "KazLLM (ISSAI)", what: "Первый крупный казахский LLM (8B/70B, 150B+ токенов).", url: "https://issai.nu.edu.kz/kazllm/" },
  { year: 2024, scope: "kazakh", label: "«Do LLMs Speak Kazakh?»", what: "Первая системная оценка казахского у 7 моделей.", url: null },
  { year: 2024, scope: "global", label: "MorphScore", what: "Метрика морфем-выравнивания токенайзеров.", url: "https://arxiv.org/abs/2411.14198" },
  { year: 2025, scope: "kazakh", label: "Sherkala-Chat", what: "SOTA казахский чат, vocab 159k, fertility 4.73→2.04.", url: "https://arxiv.org/abs/2503.01493" },
  { year: 2025, scope: "kazakh", label: "Til-Core (гос.)", what: "morphBPE 256k, громкий claim про морфологию, 0 опубликованных бенчмарков.", url: "https://huggingface.co/TilQazyna/Til-Core-0.5B" },
  { year: 2026, scope: "kazakh", label: "SozKZ + KazByte", what: "From-scratch SLM (50k BPE) и tokenizer-free (байтовый адаптер).", url: "https://arxiv.org/abs/2603.20854" },
];

export const FLAGSHIP_MODELS: FlagshipModel[] = [
  {
    name: "Til-Core-0.5B", org: "Тіл Қазына (гос.)", year: "2025", params: "497M", base: "Qwen2",
    vocab: "256 000", tokenizer: "morphBPE — BPE с запретом слияний через морфемные границы (сегментатор BiLSTM)",
    morphClaim: "ДА — но сегментатор не выложен", benchmarks: "НЕТ — ноль", highlight: true,
    note: "Громкий claim про морфологию + ноль опубликованных бенчмарков. Никто не проверял независимо.",
    url: "https://huggingface.co/TilQazyna/Til-Core-0.5B",
  },
  {
    name: "Sherkala-Chat-8B", org: "Inception / MBZUAI", year: "2025", params: "8B", base: "Llama-3.1",
    vocab: "159 766", tokenizer: "расширенный BPE (+25% к Llama-3.1)",
    morphClaim: "нет (fertility-driven)", benchmarks: "да", highlight: false,
    note: "Fertility казахского 4.73 → 2.04. Морфем-выравнивание не обсуждается.",
    url: "https://arxiv.org/abs/2503.01493",
  },
  {
    name: "SozKZ (50M–600M)", org: "S. Tukenov", year: "2026", params: "50–600M", base: "Llama-arch",
    vocab: "50 000", tokenizer: "ByteLevel BPE с нуля на казахском",
    morphClaim: "нет", benchmarks: "частично", highlight: false,
    note: "Аргумент через fertility, не через морфемные границы.",
    url: "https://arxiv.org/abs/2603.20854",
  },
  {
    name: "KazByte", org: "R. Akylzhanov", year: "2026", params: "adapter→Qwen2.5-7B", base: "Qwen2.5",
    vocab: "— (byte-level)", tokenizer: "обходит токенайзер целиком (байтовый адаптер)",
    morphClaim: "n/a — нет токенайзера", benchmarks: "да", highlight: false,
    note: "Контрапункт всему полю: «tokenizer tax» решают, убирая токенайзер.",
    url: "https://arxiv.org/abs/2603.27859",
  },
  {
    name: "KazLLM (8B / 70B)", org: "ISSAI / NU", year: "2024", params: "8B, 70B", base: "Llama-3.1",
    vocab: "128 256 (Llama-3.1)", tokenizer: "наследует Llama-3.1, расширение не документировано",
    morphClaim: "нет", benchmarks: "да (task-perf)", highlight: false,
    note: "150B+ токенов, 4 языка. Нет отдельной токенайзер-работы.",
    url: "https://issai.nu.edu.kz/kazllm/",
  },
  {
    name: "KazRoBERTa", org: "ISSAI / NU", year: "2022", params: "~125M", base: "RoBERTa",
    vocab: "32 000", tokenizer: "BPE только на казахском",
    morphClaim: "нет", benchmarks: "частично", highlight: false,
    note: "Старый baseline. Используется в гибридных морфо-анализаторах.",
    url: "https://huggingface.co/issai",
  },
];

export const GAPS: Gap[] = [
  {
    title: "Независимый аудит морфем-выравнивания казахских токенайзеров",
    yours: true,
    why: "Никто не сравнивал несколько КАЗАХСКИХ токенайзеров (KazRoBERTa, SozKZ, Sherkala, Til-Core) по морфемным границам на едином gold-стандарте. Arnett 2025 берёт казахский как 1 из 70 языков и только дженерик-токенайзеры; Duisenova 2026 строит новый, но не аудирует существующие.",
    effort: "ШИПАБЕЛЬНО на этой неделе",
  },
  {
    title: "Эмпирическая проверка claim Til-Core про морфологию",
    yours: true,
    why: "Til-Core вышел с НУЛЁМ опубликованных бенчмарков и громким заявлением «поддержка казахской морфологии». Стань первым, кто измерил это независимо.",
    effort: "входит в аудит",
  },
  {
    title: "Precision-метрика морфем-выравнивания (не только recall)",
    yours: true,
    why: "Опубликованный MorphScore меряет RECALL морфемных границ. Precision (сколько границ токенайзера реальны) и F1 для казахского никто не считал. Чистая дифференциация от Arnett & Bergen.",
    effort: "малая добавка к аудиту",
  },
  {
    title: "Совместная таблица fertility × morpheme-alignment",
    yours: false,
    why: "Sherkala репортит fertility, MorphScore-работа репортит alignment — но никто не свёл обе оси для казахских токенайзеров в одну таблицу.",
    effort: "средняя",
  },
  {
    title: "Usage-vs-morphology divergence (что носители реально говорят)",
    yours: true,
    why: "Морфологически правильная форма ≠ форма, которую носитель употребляет (напр. «біздің кітаптар» вместо «кітаптарымыз», «неге» как монолит). Это методологически не покрыто ни одной работой. Опрос носителей → новый угол.",
    effort: "мини-опрос, 30–50 ответов",
  },
];
