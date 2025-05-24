# Example Output: Incident Response Plan for Ransomware

- **Initial Detection**:
  - Monitor endpoints and SIEM for unusual encryption activity.
  - Alert triggered by Trend Micro or CrowdStrike detection rules.

- **Containment**:
  - Disconnect affected systems from network.
  - Block malicious IPs and URLs in firewall and endpoint tools.

- **Eradication**:
  - Run full scan using EDR tools.
  - Remove malicious executables and scripts.

- **Recovery**:
  - Restore systems from verified clean backups.
  - Reset user credentials and validate system integrity.

- **Post-Incident Activities**:
  - Conduct forensic analysis to determine attack vector.
  - Document findings and update IR playbooks per NIST SP 800-61.
