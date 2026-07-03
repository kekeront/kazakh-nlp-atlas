import Link from "next/link";
import type { Metadata } from "next";
import { HypothesisList, PainPointList } from "@/components/Contribute";
import { Ornament } from "@/components/Ornament";
import { Reveal } from "@/components/Reveal";
import { SectionHead } from "@/components/SectionHead";
import { HYPOTHESES, PAIN_POINTS } from "@/lib/openProblems";

export const metadata: Metadata = {
  title: "Что делать сейчас · Атлас казахского NLP",
  description:
    "Болевые точки и непроверенные гипотезы казахского NLP с цитатами — точки входа для первого вклада в исследования.",
};

export default function ContributePage() {
  return (
    <main className="wrap">
      <header className="mast" style={{ paddingTop: "56px" }}>
        <div className="kicker">Точка входа · для первого вклада</div>
        <h1>Что можно сделать&nbsp;сейчас?</h1>
        <div className="sub-en">Open problems for your first contribution</div>
        <p className="lead">
          Не нужно изобретать новую парадигму. Поле полно конкретных, недокрытых дыр и заявлений,
          которые никто не проверил. Ниже — болевые точки и непроверенные гипотезы казахского NLP,
          каждая с цитатой на реальную работу. Бери ту, что по силам, и делай первый вклад.
        </p>
      </header>

      <div className="howto">
        <b>Как читать.</b> «Болевые точки» — то, чего в поле не хватает (данные, бенчмарки, метрики);
        у каждой — конкретный первый шаг. «Непроверенные гипотезы» — то, что заявлено или
        подразумевается, но не доказано; у каждой — как это протестировать. Бейдж сложности:{" "}
        <span className="diff low" style={{ marginLeft: 0 }}>лёгкий старт</span> подходит для первой работы.
      </div>

      <Ornament />
      <Reveal>
        <section>
          <SectionHead idx="A" title="Болевые точки" sub={`${PAIN_POINTS.length} · с цитатами`} />
          <PainPointList />
        </section>
      </Reveal>

      <Ornament color="#e08a4a" />
      <Reveal>
        <section>
          <SectionHead idx="B" title="Непроверенные гипотезы" sub={`${HYPOTHESES.length} · можно протестировать`} />
          <HypothesisList />
        </section>
      </Reveal>

      <Link className="back" href="/">← назад в Атлас</Link>
    </main>
  );
}
