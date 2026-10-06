import "./globals.css";

export const metadata = { title: "FixIt Assistant", description: "AI troubleshooting for factory technicians" };

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
