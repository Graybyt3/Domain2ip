# 💚 Domain2IP Resolver 💚

A multithreaded Python script designed to resolve domain names to IP addresses. Intended for security professionals and system administrators to process domain lists efficiently, with real-time output and file generation.

---

## 🔥 Features

- **Multithreaded Resolution**: Utilizes `concurrent.futures` for parallel domain resolution, configurable via user-specified thread count.
- **Real-Time File Writing**: Appends resolved IP addresses to `ip.txt` immediately upon resolution.
- **Unique IP Generation**: Creates `unique.txt` with a sorted list of unique IPs after execution.
- **Terminal Output**: 
  - Success messages in green with underlining: `[+] domain > ip`.
  - Failure messages in red: `[-] domain > FuCK`.
  - Uses `colorama` for cross-platform compatibility.
- **Encoding Support**: Attempts multiple encodings (`utf-8`, `latin-1`, `ascii`, `utf-16`, `iso-8859-1`), continuing if one fails.
- **Timeout Handling**: Sets a 2-second timeout per domain resolution to prevent delays.
- **User Input**: Prompts for input filename and thread count at runtime.
- **ASCII Art**: Displays a multi-colored ASCII banner at startup.
- **Cross-Platform**: Compatible with Linux and Windows when `colorama` is installed.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Graybyt3/domain2ip-resolver.git
   cd domain2ip-resolver

# 👨🏻‍💻 FOR MORE INFORMATION AND SUPPORT 👨🏻‍💻

[TELEGRAM](https://t.me/rex_cc) | 
[FACEBOOK](https://www.facebook.com/graybyt3) | 
[X](https://x.com/gray_byte) | 
[INSTAGRAM](https://www.instagram.com/gray_byte)
