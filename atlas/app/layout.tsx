import type { Metadata } from "next";
import { Playfair_Display, Lora, IBM_Plex_Mono } from "next/font/google";
import { Nav } from "@/components/Nav";
import "./globals.css";

// Cyrillic-capable type — the atlas is in Russian, so every family must carry кириллица.
const disp = Playfair_Display({
  subsets: ["latin", "cyrillic"],
  weight: ["400", "600", "700"],
  style: ["normal", "italic"],
  variable: "--font-disp",
  display: "swap",
});
const serif = Lora({
  subsets: ["latin", "cyrillic"],
  weight: ["400", "500", "600"],
  variable: "--font-serif",
  display: "swap",
});
const mono = IBM_Plex_Mono({
  subsets: ["latin", "cyrillic"],
  weight: ["400", "500", "600"],
  variable: "--font-mono",
  display: "swap",
});

export const metadata: Metadata = {
  title: "Атлас казахского NLP · The State of Kazakh NLP Research",
  description:
    "Интерактивный атлас исследований казахского NLP: 222 работы, граф цитирований, " +
    "линия мировых прорывов и карта открытых контрибьюшенов.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ru" className={`${disp.variable} ${serif.variable} ${mono.variable}`}>
      <body>
        <Nav />
        {children}
      </body>
    </html>
  );
}
