import { Chronology } from "@/components/Chronology";
import { CitationGraph } from "@/components/CitationGraph";
import { FlagshipTable } from "@/components/FlagshipTable";
import { Footer } from "@/components/Footer";
import { GapMap } from "@/components/GapMap";
import { Masthead } from "@/components/Masthead";
import { Ornament } from "@/components/Ornament";
import { PaperExplorer } from "@/components/PaperExplorer";
import { Reveal } from "@/components/Reveal";
import { SectionHead } from "@/components/SectionHead";
import { StatsBand } from "@/components/StatsBand";
import { Territories } from "@/components/Territories";
import { TimelineBars } from "@/components/TimelineBars";

export default function Page() {
  return (
    <main className="wrap">
      <Masthead />
      <Reveal><StatsBand /></Reveal>

      <Ornament />
      <Reveal>
        <section>
          <SectionHead idx="01" title="Хронология поля" sub="объём работ по годам" />
          <TimelineBars />
        </section>
      </Reveal>

      <Ornament />
      <Reveal>
        <section>
          <SectionHead idx="02" title="Линия прорывов" sub="мир ⟷ казахский · виден лаг" />
          <Chronology />
        </section>
      </Reveal>

      <Ornament />
      <Reveal>
        <section>
          <SectionHead idx="03" title="Территории" sub="по убыванию открытости" />
          <Territories />
        </section>
      </Reveal>

      <Ornament />
      <Reveal>
        <section>
          <SectionHead idx="04" title="Граф цитирований" sub="размер = влияние · цвет = тема" />
          <CitationGraph />
        </section>
      </Reveal>

      <Ornament />
      <Reveal>
        <section>
          <SectionHead idx="05" title="Флагманские модели" sub="claim ≠ проверено" />
          <FlagshipTable />
        </section>
      </Reveal>

      <Ornament color="#e08a4a" />
      <Reveal>
        <section>
          <SectionHead idx="06" title="Незанятые земли" sub="где открыт контрибьюшен" />
          <GapMap />
        </section>
      </Reveal>

      <Ornament />
      <Reveal>
        <section>
          <SectionHead idx="07" title="Корпус работ" sub="arXiv + Semantic Scholar" />
          <PaperExplorer />
        </section>
      </Reveal>

      <Footer />
    </main>
  );
}
