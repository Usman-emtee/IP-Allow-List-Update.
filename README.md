# IP Allow List Update Algorithm

## Overview
This repository presents a Python algorithm to automate updating an IP allow list by removing restricted IP addresses, enhancing access control for an organization’s restricted content. Documented in a PDF, the project reads `allow_list.txt`, removes IPs listed in `remove_list`, and updates the file. It showcases my Python skills, problem-solving, and commitment to securing organizations, aligning with NIST CSF PR.AC-4 and relating to web security by restricting unauthorized access.

## Objectives
- Automate IP allow list updates using Python file I/O.
- Ensure secure access control by removing unauthorized IPs.
- Document the process in a PDF for clarity.

## Tools Used
- **Framework**: NIST CSF (PR.AC-4: Access Permissions).
- **Programming**: Python (file I/O, list manipulation).
- **Documentation**: PDF report, Markdown, screenshots.

## Repository Structure
- `ip_allow_list_update.pdf`: Project description and code snippets.
- `scripts/`: Python script for updating the allow list.

## Key Features
- **Algorithm**:
  - Reads `allow_list.txt` into a string using `with open()`.
  - Converts to a list with `.split()`.
  - Removes IPs from `remove_list` using a `for` loop and `.remove()`.
  - Writes updated list back with `.join()` and `write()`.
- **Impact**: Enhances security by restricting access, preventing unauthorized web attacks (e.g., SQL injection).
- **Recommendations**:
  - Regularly update `remove_list` based on threat intelligence.
  - Integrate with a firewall for real-time IP blocking.
  - Log changes for auditing.

## Usage
1. Clone the repository: `git clone https://github.com/yourusername/IP-Allow-List-Update.git`
2. Review the project in `ip_allow_list_update.pdf`.
3. Run the script: `python scripts/update_allow_list.py`.
4. View input/output in `data/` and screenshots in `evidence/`.

## Disclaimer
This project uses a fictional scenario. Always test automation scripts in a controlled environment.

## Contact
- GitHub: [usman-emtee](https://github.com/usman-emtee)
- LinkedIn: [usman-mt](https://linkedin.com/in/usman-mt)
- Email: usmanemtee@gmail.com
