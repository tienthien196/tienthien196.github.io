                          +---------------------+
                          |   AttackSimulator   | ← Kích hoạt tấn công
                          +----------+----------+
                                     |
                                     v
        +-----------------------------------------------------------------------------------------+
        |                             Security360 Core Engine                                     |
        |                                                                                         |
        |    +--------------+     +----------------+     +------------------+                    |
        |    |   Event      |<--->|   Logger       |<--->|   Module Manager  |                   |
        |    |  Manager     |     | (SecurityLogger)|     | (SecurityModule)  |                   |
        |    +------+-------+     +----------------+     +------------------+                    |
        |           |                                                                             |
        +-----------+-----------------------------------------------------------------------------+
                    |
                    v
     +------------------------------------------------------------------------------------------------+
     |                Các Module Bảo Mật Tích Hợp (Tương tác qua Event Bus)                            |
     |                                                                                                |
     |   Network       Data         App         System       Advanced        Compliance     Mobile    |
     |   Firewall      Encryption   WAF         PatchMgr     MalwareAnalyzer  AuditChecker   DeviceAuth |
     |   IDS/IPS       DLP          SecureCode  VulnScan     Sandbox          ConfigComp     ...       |
     |                                                                                                |
     +------------------------------------------------------------------------------------------------+


