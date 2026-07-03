import { FLAGSHIP_MODELS } from "@/lib/curated";

export function FlagshipTable() {
  return (
    <div className="tbl-scroll">
      <table>
        <thead>
          <tr>
            <th>Модель</th><th>Год</th><th>Параметры</th><th>База</th>
            <th>Vocab</th><th>Токенайзер</th><th>Морфология?</th><th>Бенчмарки?</th>
          </tr>
        </thead>
        <tbody>
          {FLAGSHIP_MODELS.map((m) => {
            const benchNo = /нет|ноль/i.test(m.benchmarks);
            const morphYes = /^да/i.test(m.morphClaim);
            return (
              <tr key={m.name} className={m.highlight ? "hl" : ""}>
                <td>
                  <a href={m.url} target="_blank" rel="noopener noreferrer">
                    <span className="mdl">{m.name}</span>
                  </a>
                  <div className="org">{m.org}</div>
                  <div className="rownote">{m.note}</div>
                </td>
                <td className="mono">{m.year}</td>
                <td className="mono">{m.params}</td>
                <td className="mono">{m.base}</td>
                <td className="mono">{m.vocab}</td>
                <td>{m.tokenizer}</td>
                <td className={morphYes ? "yes" : "mono"}>{m.morphClaim}</td>
                <td className={benchNo ? "no" : "yes"}>{m.benchmarks}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
