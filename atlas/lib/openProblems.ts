// Open problems for first-time Kazakh-NLP contributors.
// Cited pain points + unproven hypotheses, grounded in the scraped corpus by a
// research agent (June 2026). Every citation is a real, verifiable source.

import type { Hypothesis, PainPoint } from "./types";

export const PAIN_POINTS: PainPoint[] = [
  {
    title: "Высокая «стоимость токенизации» казахского текста",
    detail:
      "Многоязычные токенизаторы (BPE, SentencePiece), обученные преимущественно на высокоресурсных языках, фрагментируют казахские слова в 3–5 раз больше, чем английские — это укорачивает эффективное контекстное окно и увеличивает стоимость вычислений. KazByte называет этот «tokenizer tax» главной мотивацией, SozKZ обходит проблему обучением токенизатора с нуля.",
    category: "tokenization",
    difficulty: "low",
    firstStep:
      "Измерить fertility существующих токенизаторов (GPT-4o, LLaMA-3, Qwen2.5) на стандартизированном казахском тексте и сравнить с турецким и английским бейслайнами.",
    citations: [
      { title: "KazByte: Adapting Qwen models to Kazakh via Byte-level Adapter", url: "https://arxiv.org/abs/2603.27859", arxiv: "2603.27859" },
      { title: "SozKZ: Training Efficient Small Language Models for Kazakh from Scratch", url: "https://arxiv.org/abs/2603.20854", arxiv: "2603.20854" },
      { title: "Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh", url: "https://arxiv.org/abs/2503.01493", arxiv: "2503.01493" },
    ],
  },
  {
    title: "Нет стандартизированного бенчмарка для морфологии",
    detail:
      "Несмотря на множество работ по морфоанализу казахского, нет единого публичного набора с золотой разметкой морфемных границ и POS-тегов для воспроизводимого сравнения. Разные схемы аннотации делают сопоставление результатов невозможным.",
    category: "morphology",
    difficulty: "medium",
    firstStep:
      "Собрать 1000–2000 предложений из открытых источников (KazNERD, Wikipedia), разметить морфемы по единой схеме и опубликовать как микробенчмарк.",
    citations: [
      { title: "LLM-Assisted Weak Supervision for Low-Resource Kazakh Sequence Labeling", url: "https://www.semanticscholar.org/paper/f5369fb02d1f2a7d23bff98c36d83beb83253d64", arxiv: null },
      { title: "Machine Learning Methods for Kazakh Morphology: A Comprehensive Overview", url: "https://www.semanticscholar.org/paper/0b442d1982562ae426e97c00adff8c0d75b416ad", arxiv: null },
      { title: "NLP and Speech Technologies for Central Asian Turkic Languages: A Review", url: "https://www.semanticscholar.org/paper/d7884383dea838a61e7ba58b19ba98c7005d200c", arxiv: null },
    ],
  },
  {
    title: "Слабая поддержка казахско-русского кодового переключения",
    detail:
      "Носители регулярно переключаются между казахским и русским в одном высказывании (intra-sentential code-switching), но большинство ASR/NLP-систем обучены на монолингвальных данных. KSC2 содержит такие образцы, но их доля мала, а специализированных датасетов почти нет.",
    category: "dataset-corpus",
    difficulty: "medium",
    firstStep:
      "На базе открытого датасета отзывов (100K Movie Reviews from Kazakhstan) разметить долю code-switched фраз и опубликовать статистику как baseline.",
    citations: [
      { title: "Low-resource Machine Translation for Code-switched Kazakh-Russian", url: "https://arxiv.org/abs/2503.20007", arxiv: "2503.20007" },
      { title: "KSC2: An Industrial-Scale Open-Source Kazakh Speech Corpus", url: "https://www.semanticscholar.org/paper/e6fb05d5e2d488b15c6fb516d1b66668bf5f15d4", arxiv: null },
      { title: "100,000+ Movie Reviews from Kazakhstan: Russian, Kazakh, and Code-Switched", url: "https://arxiv.org/abs/2605.08600", arxiv: "2605.08600" },
    ],
  },
  {
    title: "Нет унифицированного набора метрик оценки LLM",
    detail:
      "Бенчмарки для казахского фрагментированы: KazMMLU, TUMLU, KazQAD, Qorgau, KZ-SafetyPrompts используют разные протоколы, модели и метрики. Объективно сравнить прогресс между работами нельзя — нет единого leaderboard.",
    category: "evaluation",
    difficulty: "low",
    firstStep:
      "Прогнать 3–5 публичных LLM на всех существующих казахских бенчмарках по единому протоколу и опубликовать сравнительную таблицу.",
    citations: [
      { title: "KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge", url: "https://arxiv.org/abs/2502.12829", arxiv: "2502.12829" },
      { title: "TUMLU: A Unified Native Language Understanding Benchmark for Turkic Languages", url: "https://arxiv.org/abs/2502.11020", arxiv: "2502.11020" },
      { title: "KazQAD: Kazakh Open-Domain Question Answering Dataset", url: "https://arxiv.org/abs/2404.04487", arxiv: "2404.04487" },
      { title: "Qorgau: Evaluating LLM Safety in Kazakh-Russian Bilingual Contexts", url: "https://arxiv.org/abs/2502.13640", arxiv: "2502.13640" },
    ],
  },
  {
    title: "ASR для спонтанной и детской речи почти отсутствует",
    detail:
      "Большинство казахских ASR обучены на дикторской речи (новости, книги, парламент). Детская речь, спонтанный диалог, телефонные разговоры и акцент представлены минимально: датасет детской речи собран только у детей 2–9 лет через Telegram-бот.",
    category: "speech",
    difficulty: "medium",
    firstStep:
      "На доступных KSC2 и Common Voice провести анализ ошибок WER в разбивке по акценту, полу и возрасту дикторов и опубликовать диагностику.",
    citations: [
      { title: "Fine-Tuning Neural ASR for Low-Resource Kazakh Children's Speech", url: "https://www.semanticscholar.org/paper/926ee5731a9c5a925876a6c51026e94402af53cb", arxiv: null },
      { title: "A Crowdsourced Open-Source Kazakh Speech Corpus and Initial Baseline", url: "https://arxiv.org/abs/2009.10334", arxiv: "2009.10334" },
      { title: "Hybrid LLM-ASR Methodology for Kazakh Language Learning", url: "https://www.semanticscholar.org/paper/5fec6730159a772f45ecb2f2f5780d72c47911a8", arxiv: null },
    ],
  },
  {
    title: "OCR для арабского и латинского казахского письма почти не существует",
    detail:
      "KazakhOCR показал, что все мультимодальные LLM (Gemma-3, Qwen2.5-VL, Llama-3.2-Vision) полностью провалились на казахском арабском и латинском скриптах, путая их с арабским/персидским. Публичного датасета реальных (не синтетических) изображений нет.",
    category: "dataset-corpus",
    difficulty: "low",
    firstStep:
      "Собрать 200–500 фото реальных вывесок, газет и документов на казахском арабском/латинском письме, разметить и опубликовать как малый benchmark.",
    citations: [
      { title: "KazakhOCR: A Synthetic Benchmark for Low-Resource Kazakh Script OCR", url: "https://arxiv.org/abs/2603.13238", arxiv: "2603.13238" },
      { title: "KOHTD: Kazakh Offline Handwritten Text Dataset", url: "https://arxiv.org/abs/2110.04075", arxiv: "2110.04075" },
      { title: "HKR For Handwritten Kazakh & Russian Database", url: "https://arxiv.org/abs/2007.03579", arxiv: "2007.03579" },
    ],
  },
  {
    title: "Эмоциональные / паралингвистические ресурсы ограничены одним датасетом",
    detail:
      "KazEmoTTS — единственный публичный корпус эмоциональной казахской речи (74 ч, 6 эмоций). Для распознавания эмоций в спонтанной речи и мультимодального анализа этого мало. Probing Whisper показал, что эмоция концентрируется в средних слоях, но downstream-экспериментов нет.",
    category: "speech",
    difficulty: "medium",
    firstStep:
      "Дообучить open-source модель распознавания эмоций на KazEmoTTS и сделать zero-shot оценку на Common Voice Kazakh для бейслайна.",
    citations: [
      { title: "KazEmoTTS: A Dataset for Kazakh Emotional Text-to-Speech Synthesis", url: "https://arxiv.org/abs/2404.01033", arxiv: "2404.01033" },
      { title: "Layer-Wise Probing of Paralinguistic Attributes in Fine-Tuned Whisper for Kazakh", url: "https://www.semanticscholar.org/paper/29f4619f35d0b172659ef407634992714c616e8a", arxiv: null },
      { title: "A Multimodal Framework for Speech Emotion Recognition in Low-Resource Languages", url: "https://www.semanticscholar.org/paper/e0fff8646106217703d97fb9756f1bfc395a42f9", arxiv: null },
    ],
  },
  {
    title: "NER не охватывает специализированные домены (медицина, право)",
    detail:
      "KazNERD обучен на телевизионных новостях. Юридические, медицинские и научные тексты имеют иную терминологию и сущности; работы по post-editing перевода отмечают наибольшие проблемы именно в юридическом (+17%) и медицинском (+22%) доменах.",
    category: "ner-ie",
    difficulty: "medium",
    firstStep:
      "Взять открытые казахские нормативные акты (data.egov.kz), разметить 500 предложений по схеме KazNERD и оценить zero-shot перенос существующих моделей.",
    citations: [
      { title: "KazNERD: Kazakh Named Entity Recognition Dataset", url: "https://arxiv.org/abs/2111.13419", arxiv: "2111.13419" },
      { title: "Enhancing Post-Editing of Kazakh Translations Using Fine-Tuned LLMs", url: "https://www.semanticscholar.org/paper/640e45a4a50e9b4cd277bb6ac1e4e72a090c4c56", arxiv: null },
    ],
  },
  {
    title: "Параллельные корпуса для большинства языковых пар малы",
    detail:
      "KazParC — первый крупный публичный параллельный корпус (kk–en–ru–tr, ~372K предложений), но покрывает лишь 4 языка. Пары kk–zh, kk–uz, kk–ky используются в обучении, но проверенных корпусов минимум, что ограничивает качество перевода.",
    category: "machine-translation",
    difficulty: "low",
    firstStep:
      "С помощью NLLB и монолингвальных корпусов построить синтетический параллельный датасет kk–uz или kk–ky и оценить его через back-translation BLEU.",
    citations: [
      { title: "KazParC: Kazakh Parallel Corpus for Machine Translation", url: "https://arxiv.org/abs/2403.19399", arxiv: "2403.19399" },
      { title: "No One-Size-Fits-All: Translation to Bashkir, Kazakh, Kyrgyz, Tatar, Chuvash", url: "https://arxiv.org/abs/2602.04442", arxiv: "2602.04442" },
      { title: "Adapting Open-Source AI Models for MT of Low-Resource Turkic Languages", url: "https://www.semanticscholar.org/paper/866c4bf9a9bf35fb2debcebe848dde7c11a44117", arxiv: null },
    ],
  },
  {
    title: "Датасеты тональности охватывают только отзывы, не все жанры",
    detail:
      "KazSAnDRA — крупнейший публичный датасет тональности (180K), но состоит только из потребительских отзывов. Новости, соцсети, политические заявления почти не представлены, что ограничивает применимость классификаторов.",
    category: "classification",
    difficulty: "low",
    firstStep:
      "Разметить 500–1000 казахских новостных заголовков по трёхклассовой схеме тональности и оценить перенос модели KazSAnDRA.",
    citations: [
      { title: "KazSAnDRA: Kazakh Sentiment Analysis Dataset of Reviews and Attitudes", url: "https://arxiv.org/abs/2403.19335", arxiv: "2403.19335" },
      { title: "100,000+ Movie Reviews from Kazakhstan: Russian, Kazakh, and Code-Switched", url: "https://arxiv.org/abs/2605.08600", arxiv: "2605.08600" },
    ],
  },
  {
    title: "У эмбеддингов нет стандартного intrinsic-бенчмарка",
    detail:
      "Кросс-языковые эмбеддинги для тюркских языков изучались, но для казахского нет публичного набора аналогий или SimLex-подобного ресурса, позволяющего сравнивать качество эмбеддингов без downstream-задачи.",
    category: "embeddings",
    difficulty: "low",
    firstStep:
      "Перевести подмножество SimLex-999 или BATS на казахский с носителями и опубликовать как первый intrinsic-бенчмарк для казахских эмбеддингов.",
    citations: [
      { title: "Cross-Lingual Word Embeddings for Turkic Languages", url: "https://arxiv.org/abs/2005.08340", arxiv: "2005.08340" },
      { title: "Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Family", url: "https://arxiv.org/abs/2604.06202", arxiv: "2604.06202" },
    ],
  },
  {
    title: "Пунктуация и нормализация ASR-вывода почти не изучены",
    detail:
      "Единственная работа по восстановлению пунктуации/капитализации для казахского использует только Wikipedia и книги и сообщает низкий F1 для редких знаков (восклицательный: F1=32.85). Нормализация ASR-вывода в реальных приложениях не решена.",
    category: "speech",
    difficulty: "low",
    firstStep:
      "Дообучить punctuation-restoration модель на транскрипциях KSC2 и сравнить с Wikipedia-бейслайном по F1 для всех классов знаков.",
    citations: [
      { title: "Restoring Punctuation and Capitalization in Kazakh: A BERT-Based Approach", url: "https://www.semanticscholar.org/paper/a0b96af0f023e6d175b99ffb89e84eccb2b5a089", arxiv: null },
      { title: "Multi-lingual meeting minutes-taking system: design and implementation", url: "https://www.semanticscholar.org/paper/9906df6aee76991dbb6e08c12dcd951ff9eae861", arxiv: null },
    ],
  },
];

export const HYPOTHESES: Hypothesis[] = [
  {
    claim: "Морфологически осведомлённая сегментация улучшает downstream-задачи на казахском по сравнению с BPE",
    status: "contested",
    detail:
      "Интуиция «учёт морфемных границ должен помогать агглютинативным языкам» широко распространена. Но Sälevä & Lignos (2021) на задаче kk–en перевода показали, что морфо-методы (LMVR, MORSEL) не дают стабильного преимущества над BPE — лучший метод варьируется, результаты статистически неразличимы.",
    howToTest:
      "Сравнить BPE-токенизатор SozKZ (50K) с морфо-сегментатором (Morfessor) на трёх задачах — NER, MT, masked LM — по единому протоколу на одних данных.",
    difficulty: "medium",
    citations: [
      { title: "The Effectiveness of Morphology-aware Segmentation in Low-Resource NMT", url: "https://arxiv.org/abs/2103.11189", arxiv: "2103.11189" },
      { title: "SozKZ: Training Efficient Small Language Models for Kazakh from Scratch", url: "https://arxiv.org/abs/2603.20854", arxiv: "2603.20854" },
    ],
  },
  {
    claim: "Байтовая (byte-level) токенизация превосходит BPE для казахского из-за агглютинативности",
    status: "unverified",
    detail:
      "KazByte выдвигает гипотезу, что сырые байты через адаптер к замороженному Qwen2.5-7B сравняются или превзойдут оригинал. Авторы прямо пишут «эмпирическая валидация продолжается» — опубликованных сравнений нет. Для других языков byte-level не дал однозначного преимущества.",
    howToTest:
      "Дообучить ByT5-small на казахском (OSCAR/CC100) и сравнить с BPE-моделью того же размера на KazMMLU и KazQAD.",
    difficulty: "medium",
    citations: [
      { title: "KazByte: Adapting Qwen models to Kazakh via Byte-level Adapter", url: "https://arxiv.org/abs/2603.27859", arxiv: "2603.27859" },
      { title: "SozKZ: Training Efficient Small Language Models for Kazakh from Scratch", url: "https://arxiv.org/abs/2603.20854", arxiv: "2603.20854" },
    ],
  },
  {
    claim: "Перенос от турецкого эффективнее переноса от русского для казахских задач",
    status: "assumed",
    detail:
      "Типологическая близость казахского и турецкого (агглютинация, гармония гласных, SOV) часто приводится как обоснование cross-lingual transfer, но систематического сравнения «от турецкого vs от русского» на фиксированных задачах (NER, SA, QA) нет.",
    howToTest:
      "Дообучить модели на турецких и русских данных одного объёма, затем fine-tune на KazNERD и сравнить F1 на тесте.",
    difficulty: "medium",
    citations: [
      { title: "Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Family", url: "https://arxiv.org/abs/2604.06202", arxiv: "2604.06202" },
      { title: "Speech Recognition for Turkic Languages Using Cross-Lingual Transfer from Kazakh", url: "https://www.semanticscholar.org/paper/5f89dfb129c20e35aeeb69639ee964c98b05c0de", arxiv: null },
      { title: "Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages", url: "https://arxiv.org/abs/2603.21036", arxiv: "2603.21036" },
    ],
  },
  {
    claim: "Рассуждение на английском с переводом ответа на казахский сохраняет качество у современных LLM",
    status: "unverified",
    detail:
      "«Left Behind» (2026) показал, что cross-lingual transfer (CoT на английском → перевод) даёт прирост только для двуязычных архитектур и не работает для English-dominant моделей. Тем не менее стратегия часто предполагается рабочей без проверки на казахских бенчмарках.",
    howToTest:
      "На KazMMLU/KazQAD сравнить три режима — прямой ответ на казахском, CoT на казахском, CoT на английском + перевод — для 3–5 моделей.",
    difficulty: "low",
    citations: [
      { title: "Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages", url: "https://arxiv.org/abs/2603.21036", arxiv: "2603.21036" },
      { title: "KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge", url: "https://arxiv.org/abs/2502.12829", arxiv: "2502.12829" },
      { title: "Effects of Cross-lingual Evidence in Multilingual Medical Question Answering", url: "https://arxiv.org/abs/2604.20531", arxiv: "2604.20531" },
    ],
  },
  {
    claim: "Увеличение размера словаря токенизатора значимо улучшает downstream-качество казахских LLM",
    status: "unverified",
    detail:
      "SozKZ использует 50K BPE вместо 32K и показывает конкурентные результаты, но без ablation влияния именно размера словаря при фиксированном числе токенов. Sherkala обучен с расширенным словарём, но сравнения по словарю не проводилось.",
    howToTest:
      "Обучить три идентичные модели (архитектура, данные) со словарём 16K/32K/64K BPE и сравнить fertility, перплексию и F1 на NER.",
    difficulty: "high",
    citations: [
      { title: "SozKZ: Training Efficient Small Language Models for Kazakh from Scratch", url: "https://arxiv.org/abs/2603.20854", arxiv: "2603.20854" },
      { title: "Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh", url: "https://arxiv.org/abs/2503.01493", arxiv: "2503.01493" },
    ],
  },
  {
    claim: "Синтетических данных из TTS достаточно для bootstrap ASR без реальных записей",
    status: "unverified",
    detail:
      "Работа по распознаванию речевых команд (2023) дала 89.79% на TTS-синтезе. Но обобщение на непрерывную спонтанную речь не доказано: TTS даёт читаемую, а не разговорную речь, что чревато domain shift при развёртывании.",
    howToTest:
      "Дообучить Whisper только на синтезе KazakhTTS2 и сравнить WER на трёх доменах (KSC2 news, Common Voice, спонтанный чат) с моделью на реальных данных.",
    difficulty: "low",
    citations: [
      { title: "Speech Command Recognition: TTS and Speech Corpus Scraping Are All You Need", url: "https://www.semanticscholar.org/paper/56039f8f858525b520ea523252de2c31cf01de50", arxiv: null },
      { title: "KazakhTTS2: Extending the Open-Source Kazakh TTS Corpus", url: "https://arxiv.org/abs/2201.05771", arxiv: "2201.05771" },
      { title: "Improved Kazakh Named Entity Transcription Using Synthetic Speech", url: "https://www.semanticscholar.org/paper/d341fcc52aa27765e814952c9e64938cb99ebc89", arxiv: null },
    ],
  },
  {
    claim: "Промпты на казахском систематически безопаснее русских у одних и тех же LLM",
    status: "unverified",
    detail:
      "Qorgau показывает различия в safety-поведении между казахским и русским, но направление эффекта неоднородно по категориям. KZ-SafetyPrompts: GPT-4o отказывает в 28.2% казахских промптов (разброс 5.5–53.8%), но систематического kk-vs-ru сравнения на идентичных промптах нет.",
    howToTest:
      "Взять 200 промптов из Qorgau/KZ-SafetyPrompts, перевести с русского на казахский носителем и сравнить refusal rate одной модели на обеих версиях.",
    difficulty: "low",
    citations: [
      { title: "Qorgau: Evaluating LLM Safety in Kazakh-Russian Bilingual Contexts", url: "https://arxiv.org/abs/2502.13640", arxiv: "2502.13640" },
      { title: "KZ-SafetyPrompts: A Kazakh Safety Evaluation Prompt Dataset for LLMs", url: "https://arxiv.org/abs/2605.26947", arxiv: "2605.26947" },
    ],
  },
  {
    claim: "Малая модель с нуля на казахском превосходит крупную многоязычную при равном бюджете инференса",
    status: "unverified",
    detail:
      "SozKZ-600M приближается к LLaMA-3.2-1B (30.3% vs 32.0% на cultural QA) и обходит 2B-многоязычные на SIB-200 — косвенная поддержка. Но прямого сравнения при равном бюджете инференса (FLOPS/latency) с Sherkala нет, результатов на KazQAD/KazNERD тоже.",
    howToTest:
      "Сравнить SozKZ-600M с quantized Sherkala-8B на KazMMLU/KazQAD/KazNERD при равном ограничении latency (≤100ms CPU) и зафиксировать accuracy-throughput trade-off.",
    difficulty: "medium",
    citations: [
      { title: "SozKZ: Training Efficient Small Language Models for Kazakh from Scratch", url: "https://arxiv.org/abs/2603.20854", arxiv: "2603.20854" },
      { title: "Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh", url: "https://arxiv.org/abs/2503.01493", arxiv: "2503.01493" },
      { title: "KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge", url: "https://arxiv.org/abs/2502.12829", arxiv: "2502.12829" },
    ],
  },
];
