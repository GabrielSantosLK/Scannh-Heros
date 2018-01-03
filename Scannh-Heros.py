#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time

print ("""\033[33m 

 ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗██╗  ██╗
 ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██║  ██║
 ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║███████║
 ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══██║
 ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║██║  ██║
 ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝  ╚═╝\033[0;0m
\033[33m
\033[33m
 ██╗  ██╗███████╗██████╗  ██████╗ ███████╗
 ██║  ██║██╔════╝██╔══██╗██╔═══██╗██╔════╝
 ███████║█████╗  ██████╔╝██║   ██║███████╗
 ██╔══██║██╔══╝  ██╔══██╗██║   ██║╚════██║
 ██║  ██║███████╗██║  ██║╚██████╔╝███████║
 ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝\033[0;0m
 \033[33m
            +------------------------------------------------+
            | Desenvolvedor : Gabriel Santos                 |
            | Data de Criação: 01/01/2018                    |
            | Github: https://github.com/GabrielSantosLK     |
            +------------------------------------------------+\033[0;0m
                        """)
print('\033[33m\n [¿] Desejas fazer qual tipo de Scanner:\033[0;0m')
print('''\033[33m 
     [1] Scanner Via URL
     [2] Scanner Via IP
     [3] Lista de Portas de Protocolos\033[0;0m ''')


menu = int(input('\033[33m\n [!] Qual Scanner Desejas: ▬▶ \033[0;0m'))

if menu == 1:
            portas = [21, 23, 443, 8080, 3306, 80, 110, 143, 443, 523, 993, 1433, 1521, 1723, 3306, 3389, 5432, 5900] #Portas Integradas na memory do Code
            print('\033[33m\n [!] Caso o Script retorne em branco, não tem Portas Abertas!\033[0;0m') 
            alvo = input('\033[33m\n [¿] Endereço: \033[0;0m') #Endereço do Site o qual será Scanneado
            for porta in portas:#Laço For de Verificação
                        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        cliente.settimeout(0.1)
                        codigo = cliente.connect_ex((alvo, porta))
                        if codigo == 0: #Se o Status code for 0 == Tudo ok!
                                    print('\033[32m\n [!] Porta Open ▬▶ \033[0;0m',  porta)
                                    

elif menu == 2:
            ip = str(input('\033[33m\n [¿] Entre com o IP que desejas Scannear: \033[0;0m'))
            portas = [20, 21, 22, 23, 25, 43, 53, 80, 110, 143, 443, 523, 993, 1433, 1521, 1723, 3306, 3389, 5432, 5900]
            for porta in portas:
                        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        cliente.settimeout(0.1)
                        codigo = cliente.connect_ex((ip, porta))
                        if codigo == 0: #Se o Status code for 0 == Tudo ok!
                                    print('\033[32m\n [!] Porta Open ▬▶\033[0;0m ',  porta)


elif menu == 3:
            print('''\033[33m

			              [!] Lista de Portas de Protocolos!



0/TCP,UDP	Reservada.	Fora de Serviço
1/TCP,UDP	TCPMUX (Serviço de porta TCP multiplexador)	Oficial
5/TCP,UDP	RJE (Remote Job Entry - Entrada de trabalho remoto)	Oficial
7/TCP,UDP	ECHO protocol	Oficial
9/TCP,UDP	DISCARD protocol	Oficial
11/TCP,UDP	SYSTAT protocol	Oficial
13/TCP,UDP	DAYTIME protocol	Oficial
17/TCP,UDP	QOTD (Quote of the Day) protocol	Oficial
18/TCP,UDP	Message Send Protocol (Protocolo de envio de mensagem)	Oficial
19/TCP,UDP	CHARGEN protocol (Character Generator Protocol - Protocolo de geração de caracter)	Oficial
20/TCP	FTP (File Transfer protocol - Protocolo de transferência de arquivo) - data port	Oficial
21/TCP	FTP (File Transfer protocol - Protocolo de transferência de arquivo) - control (command) port	Oficial
22/TCP,UDP	SSH (Secure Shell - Shell seguro) - Usada para logins seguros, transferência de arquivos e redirecionamento de porta	Oficial
23/TCP,UDP	Telnet protocol - Comunicação de texto sem encriptação	Oficial
25/TCP,UDP	SMTP (Simple Mail Transfer Protocol - Protocolo simples de envio de e-mail) - usada para roteamento de e-mail entre servidores (Atualmente é utilizada a porta 587,conforme Comitê Gestor da Internet no Brasil CGI.br	Oficial
26/TCP,UDP	RSFTP - protocolo similar ao FTP	Não-oficial
35/TCP,UDP	QMS Magicolor 2 printer	Não-oficial
37/TCP,UDP	TIME protocol (Protocolo de Tempo)	Oficial
38/TCP,UDP	Route Access Protocol (Protocolo de Acesso ao roteador)	Oficial
39/TCP,UDP	Resource Location Protocol (Protocolo de localização de recursos)	Oficial
41/TCP,UDP	Graphics (gráficos)	Oficial
42/TCP,UDP	Host Name Server (Servidor do Nome do Host)	Oficial
42/TCP,UDP	WINS [3]	Não-oficial/Conflito
43/TCP	WHOIS (protocolo de consulta de informações de contato e DNSprotocol)	Oficial
49/TCP,UDP	TACACS Login Host protocol(Protocolo de Login no Host)	Oficial
53/TCP,UDP	DNS (Sistema de nome de domínio)	Oficial
57/TCP	MTP, Mail Transfer Protocol (Protocolo de transferência de e-mail)	
67/UDP	BOOTP (BootStrap Protocol) server; também utilizada por DHCP (Protocolo de configuração dinâmica do Host)	Oficial
68/UDP	BOOTP client; também utilizada por DHCP	Oficial
69/UDP	TFTP(Trivial File Transfer Protocol) (Protocolo de transferência de arquivo trivial)	Oficial
70/TCP	Gopher (Protocolo para indexar repositórios) protocol	Oficial
79/TCP	Finger protocol	Oficial
80/TCP	HTTP (HyperText Transfer Protocol)(Procolo de transferência de HiperTexto) - usada para transferir páginas WWW	Oficial
80/TCP	HTTP Alternate (HyperText Transfer Protocol) (Protocolo de transferência de HiperTexto)	Oficial
81/TCP	Skype protocol	Oficial
81/TCP	Torpark - Onion routing ORport	Não-oficial
82/UDP	Torpark - Control Port	Não-oficial
88/TCP	Kerberos (Protocolo de comunicações individuais seguras e identificadas) - authenticating agent	Oficial
101/TCP	HOSTNAME	
102/TCP	ISO-TSAP protocol	
107/TCP	Remote Telnet Service (Serviço remoto Telnet)	
109/TCP	POP (Post Office Protocol): Protocolo de Correio Eletrônico, versão 2	
110/TCP	POP3 (Post Office Protocol version 3): Protocolo de Correio Eletrônico, versão 3 - usada para recebimento de e-mail	Oficial
111/TCP,UDP	sun protocol (Protocolo da sun)	Oficial
113/TCP	ident - antigo identificador de servidores, ainda usada em servidores IRC para identificar seus usuários	Oficial
115/TCP	SFTP, (Simple File Transfer Protocol) (Protocolo de simples transferência de arquivo)	
117/TCP	UUCP-PATH	
118/TCP,UDP	SQL Services	Oficial
119/TCP	NNTP (Network News Transfer Protocol) (Protocolo de transferência de notícias na rede) - usada para recebimento de mensagens de newsgroups	Oficial
123/UDP	NTP (Network Time Protocol) (Protocolo de tempo na rede) - usada para sincronização de horário	Oficial
135/TCP,UDP	EPMAP (End Point Mapper) / Microsoft RPC Locator Service (Microsoft RPC Serviço de localização)	Oficial
137/TCP,UDP	NetBIOS NetBIOS Name Service	Oficial
138/TCP,UDP	NetBIOS NetBIOS Datagram Service (Serviço de datagrama NetBios)	Oficial
139/TCP,UDP	NetBIOS NetBIOS Session Service (Serviço de sessão NetBios)	Oficial
143/TCP,UDP	IMAP4 (Internet Message Access Protocol 4) (Protocolo de Acesso a mensagens na Internet) - usada para recebimento de e-mail	Oficial
152/TCP,UDP	BFTP, Background File Transfer Program (Protocolo de transferência de arquivo em Background(fundo)	
153/TCP,UDP	SGMP, Simple Gateway Monitoring Protocol (Protocolo de simples monitoramento do gateway)	
156/TCP,UDP	SQL Service (Serviço SQL)	Oficial
158/TCP,UDP	DMSP, Distributed Mail Service Protocol (Protocolo de serviço de e-mail distribuído)	
161/TCP,UDP	SNMP (Simple Network Management Protocol) (Protocolo simples de gerenciamento de rede)	Oficial
162/TCP,UDP	SNMPTRAP	Oficial
170/TCP	Print-srv (Print Server)	
179/TCP	BGP (Border Gateway Protocol)(Protocolo de limite do gateway)	Oficial
194/TCP	IRC (Internet Relay Chat)	Oficial
201/TCP,UDP	AppleTalk Routing Maintenance	
209/TCP,UDP	The Quick Mail Transfer Protocol (Protocolo de rápida transferência de mail)	
213/TCP,UDP	IPX (Internetwork Packet Exchange) (Troca de pacote na área de trabalho da internet)	Oficial
218/TCP,UDP	MPP, Message Posting Protocol (Protocolo de postagem de mensagem)	
220/TCP,UDP	IMAP, Interactive Mail Access Protocol, version 3 (Protocolo de acesso interativo ao mail)	
259/TCP,UDP	ESRO, Efficient Short Remote Operations (Operações remotas de curta eficiência)	
264/TCP,UDP	BGMP, Border Gateway Multicast Protocol	
311/TCP	Apple Server-Admin-Tool, Workgroup-Manager-Tool, (Ferramenta de gerenciamento de workgroup)	
318/TCP,UDP	TSP, Time Stamp Protocol	
323/TCP,UDP	IMMP, Internet Message Mapping Protocol (Protocolo de mapeamento de mensagem da internet)	
383/TCP,UDP	HP OpenView HTTPs Operations Agent	
366/TCP,UDP	SMTP, Simple Mail Transfer Protocol (Protocolo de simples transferência de mail). ODMR, On-Demand Mail Relay	
369/TCP,UDP	Rpc2portmap	Oficial
371/TCP,UDP	ClearCase albd	Oficial
384/TCP,UDP	A Remote Network Server System (Sistema servidor de rede remota)	
387/TCP,UDP	AURP, AppleTalk Update-based Routing Protocol	
389/TCP,UDP	LDAP (Lightweight Directory Access Protocol)(Protocolo de acesso a diretório lightweight)	Oficial
401/TCP,UDP	UPS Uninterruptible Power Supply (Suprimento de potência Ininterruptível)	Oficial
411/TCP	Direct Connect (Rede de conexão direta, Conexão direta) Hub port	Não-oficial
412/TCP	Direct Connect Client-To-Client port	Não-oficial
427/TCP,UDP	SLP (Service Location Protocol) (Protocolo de serviço de localização)	Não-oficial
443/TCP	HTTPS - HTTP Protocol over TLS/SSL (transmissão segura)(Camada de transporte seguro)	Oficial
444/TCP,UDP	SNPP, Simple Network Paging Protocol (Protocolo simples de paging de rede)	
445/TCP	Microsoft-DS (Active Directory, Windows shares, Sasser (vírus), Agobot, Zobotworm	Oficial
445/UDP	Microsoft-DS SMB (Bloco de mensagem de servidor) file sharing	Oficial
464/TCP,UDP	Kerberos Change/Set password	Oficial
465/TCP	SMTP over SSL - Conflito registrado com protocolo Cisco	Conflito
500/TCP,UDP	ISAKMP, IKE-Internet Key Exchange	Oficial
502/TCP,UDP	Modbus, Protocol	
512/TCP	exec, Remote Process Execution (Processo de execução remota)	
512/UDP	comsat, together with biff: notifica usuários acerca de novos e-mail's não lidos	
513/TCP	Login	
513/UDP	Who	
514/TCP	rsh protocol(protocolo de shell remoto) - usado para executar linha de comando não interativa em sistema remoto e visualizar a tela de retorno	
514/UDP	syslog protocol - usado para log do sistema	Oficial
515/TCP	Line Printer Daemon protocol - usada em servidores de impressão LPD	
517/UDP	Talk	
518/UDP	NTalk	
520/TCP	efs	
520/UDP	Routing - RIP (Protocolo de informação do roteador)	Oficial
513/UDP	Router	
524/TCP,UDP	NetWare Core Protocol (NCP) (Protocolo de core do NetWare)	Oficial
525/UDP	Timed, Timeserver	
530/TCP,UDP	RPC (Procedimento de chamada remota)	Oficial
531/TCP,UDP	AOL Instant Messenger, IRC Mensageiro instantâneo AOL	Não-oficial
532/TCP	netnews	
533/UDP	netwall, For Emergency Broadcasts	
540/TCP	UUCP (Unix-to-Unix Copy Protocol)	Oficial
542/TCP,UDP	commerce (Commerce Applications)	Oficial
543/TCP	klogin, Kerberos login	
544/TCP	kshell, Kerberos Remote shell	
546/TCP,UDP	DHCPv6 client	
547/TCP,UDP	DHCPv6 server	
548/TCP	AFP (Apple Filing Protocol) (Protocolo de arquivamento da Apple)	
550/UDP	new-rwho, new-who	
554/TCP,UDP	RTSP (Real Time Streaming Protocol) (Protocolo de streaming em tempo real)	Oficial
556/TCP	Remotefs, rfs, rfs_server	
560/UDP	rmonitor, Remote Monitor (Monitor remoto)	
561/UDP	monitor	
563/TCP,UDP	NNTP protocol over TLS/SSL (NNTPS)	Oficial
587/TCP	email message submission (SMTP) (RFC 2476)	Oficial
591/TCP	FileMaker 6.0 Web Sharing (alternativa ao HTTP)	Oficial
593/TCP,UDP	HTTP RPC Ep Map	Oficial
604/TCP	TUNNEL	
631/TCP,UDP	IPP, (Internet Printing Protocol) (Protocolo de impressão na internet)	
636/TCP,UDP	LDAP sobre SSL	Oficial
639/TCP,UDP	MSDP, Multicast Source Discovery Protocol (Protocolo de descoberta de fonte multicast)	
646/TCP	LDP, Label Distribution Protocol (Protocolo de distribuição de rótulo)	
647/TCP	DHCP Failover Protocol	
648/TCP	RRP, Registry Registrar Protocol (Protocolo de registro)	
652/TCP	DTCP, Dynamic Tunnel Configuration Protocol (Protocolo de configuração dinâmica de túnel)	
654/TCP	AODV, Ad hoc On-Demand Distance Vector	
665/TCP	sun-dr, Remote Dynamic Reconfiguration (Reconfiguração remota dinâmica)	Não-oficial
666/UDP	Doom, First online first-person shooter	
674/TCP	ACAP, Application Configuration Access Protocol (Protocolo de acesso a configuração da aplicação)	
691/TCP	MS Exchange Routing	Oficial
692/TCP	Hyperwave-ISP	
694/UDP	Linux-HA High availability Heartbeat port	Não-oficial
695/TCP	IEEE-MMS-SSL	
698/TCP	OLSR, Optimized Link State Routing	
699/TCP	Access Network	
700/TCP	EPP, Extensible Provisioning Protocol (Protocolo de provisionamento extensível)	
701/TCP	LMP, Link Management Protocol (Protoloco de gerenciamento de link)	
702/TCP	IRIS over BEEP	
706/TCP	SILC, Secure Internet Live Conferencing (Conferência ao vivo da seguraça da internet)	
711/TCP	TDP, Tag Distribution Protocol (Protocolo de distribuição de marcadores)	
712/TCP	TBRPF, Topology Broadcast based on Reverse-Path Forwarding	
720/TCP	SMQP, Simple Message Queue Protocol (Protocolo de simples mensagem em fila)	
749/TCP, UDP	kerberos-adm, Kerberos administration	
750/UDP	Kerberos version IV	
782/TCP	Conserver serial-console management server	
829/TCP	CMP (Certificate Management Protocol)	
860/TCP	iSCSI	
873/TCP	rsync File synchronisation protocol	Oficial
901/TCP	Samba Web Administration Tool (SWAT)	Não-oficial
902	VMware Server Console[1]	Não-oficial
904	VMware Server Alternate (se a porta 902 estiver em uso - ex: SUSE linux)	Não-oficial
911/TCP	Network Console on Acid (NCA) - local tty redirection over OpenSSH	
981/TCP	SofaWare Technologies Remote HTTPS management for firewall devices running embedded Checkpoint Firewall-1 software	Não-oficial
989/TCP,UDP	FTP Protocol (data) over TLS/SSL	Oficial
990/TCP,UDP	FTP Protocol (control) over TLS/SSL	Oficial
991/TCP,UDP	NAS (Netnews Admin System)	
992/TCP,UDP	Telnet protocol over TLS/SSL	Oficial
993/TCP	IMAP4 sobre SSL (transmissão segura)	Oficial
995/TCP	POP3 sobre SSL (transmissão segura)	Oficial
Portas 1058 a 47808[editar | editar código-fonte]
Porta	Descrição	Status
1058/tcp	nim AIX Network Installation Manager	Oficial
1059/tcp	nimreg	Oficial
1080/tcp	SOCKS proxy	Oficial
1099/tcp	RMI Registry	Oficial
1099/udp	RMI Registry	Oficial
1109/tcp	Kerberos POP	
1167/udp	phone, conference calling	
1176/tcp	Perceptive Automation Indigo home control server	Oficial
1182/tcp,udp	AcceleNet	Oficial
1194/udp	OpenVPN	Oficial
1198/tcp,udp	Cajo project. Transparência dinâmica livre de computação em Java	Oficial
1200/udp	[4] Steam Friends Applet]	Oficial
1214/tcp	Kazaa	Oficial
1223/tcp,udp	TGP: "TrulyGlobal Protocol" aka "The Gur Protocol"	Oficial
1234/tcp	TOTVS	Não-Oficial
1241/tcp,udp	Nessus Security Scanner	Oficial
1248/tcp	NSClient/NSClient++/NC_Net (Nagios)	Não-oficial
1270/tcp,udp	Microsoft Operations Manager 2005 agent (MOM 2005)	Oficial
1311/tcp	Dell Open Manage Https Port	Não-oficial
1313/tcp	Xbiim (Canvii server) Port	Não-oficial
1337/tcp	WASTE Encrypted File Sharing Program	Não-oficial
1352/tcp	IBM Lotus Notes/Domino RPC	Oficial
1387/tcp	Computer Aided Design Software Inc LM (cadsi-lm)	Oficial
1387/udp	Computer Aided Design Software Inc LM (cadsi-lm)	Oficial
1414/tcp	IBM MQSeries	Oficial
1431/tcp	RGTP	Oficial
1433/tcp,udp	Microsoft SQL database system	Oficial
1434/tcp,udp	Microsoft SQL Monitor	Oficial
1494/tcp	Citrix Presentation Server ICA Client	Oficial
1512/tcp,udp	WINS	
1514/udp	OSSEC / fujitsu-dtcns / Protocol Information and Warning	
1521/tcp	nCube License Manager	Oficial
1521/tcp	Oracle database default listener, in future releases official port 2483	Não-oficial
1522/tcp	Oracle database	
1522/udp	Oracle database	
1524/tcp	ingresslock, ingress	
1526/tcp	Oracle database common alternative for listener	Não-oficial
1533/tcp	IBM Sametime IM - Virtual Places Chat	Oficial
1547/tcp	Laplink	Oficial
1547/udp	Laplink	Oficial
1550	Gadu-Gadu (Direct Client-to-Client)	Não-oficial
1581/udp	Combat-net radio	Oficial
1589/udp	Cisco VQP (VLAN Query Protocol) / VMPS	Não-oficial
1627	iSketch	Não-oficial
1677/tcp	Novell GroupWise clients in client/server access mode	
1701/udp	l2tp, Layer 2 Tunnelling protocol	
1716/tcp	America's Army MMORPG Default Game Port	Oficial
1723/tcp	Microsoft PPTP VPN	Oficial
1723/udp	Microsoft PPTP VPN	Oficial
1725/udp	Valve Steam Client	Não-oficial
1755/tcp	Microsoft Media Services (MMS, ms-streaming)	Oficial
1755/udp	Microsoft Media Services (MMS, ms-streaming)	Oficial
1761/tcp,udp	cft-0	Oficial
1761/tcp	Novell Zenworks Remote Control utility	Não-oficial
1762-1768/tcp,udp	cft-1 to cft-7	Oficial
1812/udp	RADIUS - protocolo de autenticação	
1813/udp	radacct, (RADIUS) protocolo de conta	
1863/tcp	Windows Live Messenger	Oficial
1900/udp	Microsoft SSDP. Habilita a descoberta de dispositivos UPnP	Oficial
1935/tcp	Macromedia Flash Communications Server MX	Oficial
1970/tcp,udp	Danware Data NetOp Remote Control	Oficial
1971/tcp,udp	Danware Data NetOp School	Oficial
1972/tcp,udp	InterSystems Caché	Oficial
1975-77/udp	Cisco TCO (Documentation)	Oficial
1984/tcp	Big Brother - network monitoring tool	Oficial
1985/udp	Cisco HSRP	Oficial
2000/udp	Cisco SCCP (Skinny)	Oficial
2000/tcp	Cisco SCCP (Skinny)	Oficial
2002/tcp	Cisco Secure Access Control Server (ACS) for Windows	Não-oficial
2030	Oracle Services for Microsoft Transaction Server	Não-oficial
2031/tcp	mobrien-chat - Mike O'Brien <mike@mobrien.com> November 2004	Official
2031/udp	mobrien-chat - Mike O'Brien <mike@mobrien.com> November 2004	Official
2049/udp	nfs, NFS Server	Official
2049/udp	shilp	Official
2053/tcp	knetd, Kerberos de-multiplexor	
2056/udp	Civilization 4 multiplayer	Não-oficial
2074/tcp	Vertel VMF SA (i.e. App.. SpeakFreely)	Official
2074/udp	Vertel VMF SA (i.e. App.. SpeakFreely)	Official
2082/tcp	Infowave Mobility Server	Official
2082/tcp	CPanel, default port	Não-oficial
2083/tcp	Secure Radius Service (radsec)	Official
2083/tcp	CPanel default SSL port	Não-oficial
2086/tcp	GNUnet	Official
2086/tcp	WebHost Manager default port	Não-oficial
2087/tcp	WebHost Manager default SSL port	Não-oficial
2095/tcp	CPanel default webmail port	Não-oficial
2096/tcp	CPanel default SSL webmail port	Não-oficial
2161/tcp	?-APC Agent	Official
2181/tcp	EForward-document transport system	Official
2181/udp	EForward-document transport system	Official
2200/tcp	Tuxanci - Game Server (http://www.tuxanci.org)	Não-oficial
2219/tcp	NetIQ NCAP Protocol	Official
2219/udp	NetIQ NCAP Protocol	Official
2220/tcp	NetIQ End2End	Official
2220/udp	NetIQ End2End	Official
2222/tcp	DirectAdmin's default port	Não-oficial
2222/udp	Microsoft Office X antipiracy network monitor [5]	Não-oficial
2301/tcp	HP System Management Redirect to port 2381	Não-oficial
2302/udp	ArmA multiplayer (default for game)	Não-oficial
2302/udp	Halo: Combat Evolved multiplayer	Não-oficial
2303/udp	ArmA multiplayer (default for server reporting) (default port for game +1)	Não-oficial
2305/udp	ArmA multiplayer (default for VoN) (default port for game +3)	Não-oficial
2369/tcp	Default port for BMC Software CONTROL-M/Server - Configuration Agent port number - though often changed during installation	Não-oficial
2370/tcp	Default port for BMC Software CONTROL-M/Server - Port utilized to allow the CONTROL-M/Enterprise Manager to connect to the CONTROL-M/Server - though often changed during installation	Não-oficial
2381/tcp	HP Insight Manager default port for webserver	Não-oficial
2400/TCP,UDP	Age of Enpire II - The Conquerors	Oficial
2404/tcp	IEC 60870-5-104	Official
2427/udp	Cisco MGCP	Official
2447/tcp	ovwdb - OpenView Network Node Manager (NNM) daemon	Official
2447/udp	ovwdb - OpenView Network Node Manager (NNM) daemon	Official
2483/tcp,udp	Oracle database listening port for unsecure client connections to the listener, replaces port 1521	Official
2484/tcp,udp	Oracle database listening port for SSL client connections to the listener	Official
2546/tcp,udp	Vytal Vault - Data Protection Services	Não-oficial
2593/tcp,udp	RunUO - Ultima Online Server (http://www.runuo.com)	Não-oficial
2598/tcp	new ICA - when Session Reliability is enabled, TCP port 2598 replaces port 1494	Não-oficial
2612/tcp,udp	QPasa from MQSoftware (http://www.mqsoftware.com)	Official
2710/tcp	XBT Bittorrent Tracker	Não-oficial
2710/udp	XBT Bittorrent Tracker experimental UDP tracker extension	Não-oficial
2710/tcp	Knuddels.de	Não-oficial
2735/tcp	NetIQ Monitor Console	Official
2735/udp	NetIQ Monitor Console	Official
2809/tcp	corbaloc:iiop URL, per the CORBA 3.0.3 specification. Also used by IBM WebSphere Application Server Node Agent Official
2809/udp	corbaloc:iiop URL, per the CORBA 3.0.3 specification.	
2944/udp	Megaco Text H.248	Não-oficial
2945/udp	Megaco Binary (ASN.1) H.248	Não-oficial
2948/tcp	WAP-push Multimedia Messaging Service (MMS)	Official
2948/udp	WAP-push Multimedia Messaging Service (MMS)	Official
2949/tcp	WAP-pushsecure Multimedia Messaging Service (MMS)	Official
2949/udp	WAP-pushsecure Multimedia Messaging Service (MMS)	Official
2967/tcp	Symantec AntiVirus Corporate Edition	Não-oficial
3000/tcp	Miralix License server	Não-oficial
3000/udp	Distributed Interactive Simulation (DIS), modifiable default port	Não-oficial
3001/tcp	Miralix Phone Monitor	Não-oficial
3002/tcp	Miralix CSTA	Não-oficial
3003/tcp	Miralix GreenBox API	Não-oficial
3004/tcp	Miralix InfoLink	Não-oficial
3006/tcp	Miralix SMS Client Connector	Não-oficial
3007/tcp	Miralix OM Server	Não-oficial
3050/tcp,udp	gds_db (Interbase/Firebird)	Official
3074/tcp,udp	Xbox Live	Official
3128/tcp	HTTP used by web caches and the default port for the Squid cache	Official
3260/tcp	iSCSI target	Official
3305/tcp,udp	ODETTE-FTP	Official
3306/tcp,udp	MySQL Database system	Official
3333/tcp	Network Caller ID server	Não-oficial
3389/tcp	Microsoft Terminal Server (RDP) officially registered as Windows Based Terminal (WBT)	Official
3396/tcp	Novell NDPS Printer Agent	Official
3689/tcp	DAAP Digital Audio Access Protocol used by Apple’s iTunes	Official
3690/tcp	Subversion version control system	Official
0000/não é seguro	World of Warcraft Online gaming MMORPG	Official
3784/tcp	Ventrilo VoIP program used by Ventrilo	Official
3785/udp	Ventrilo VoIP program used by Ventrilo	Official
3872/tcp	Oracle Management Remote Agent	Não-oficial
3900/tcp	Unidata UDT OS udt_os	Official
3945/tcp	Emcads server service port, a Giritech product used by G/On	Official
4000/tcp	remoteanything
4007/tcp	PrintBuzzer printer monitoring socket server	Não-oficial
4089/udp	OpenCORE Remote Control Service	Official
4089/tcp	OpenCORE Remote Control Service	Official
4093/udp	PxPlus Client server interface ProvideX	Official
4093/tcp	PxPlus Client server interface ProvideX	Official
4100	WatchGuard Authentication Applet - default port	Não-oficial
4111/tcp,udp	Xgrid	Official
4111/tcp	Microsoft Office SharePoint Portal Server - default administration port	Não-oficial
4226/tcp,udp	Aleph One (computer game)	Não-oficial
4224/tcp	Cisco CDP Cisco discovery Protocol	???
4569/udp	Inter-Asterisk eXchange - IAX	Não-oficial
4662/tcp	eMule - port often used	Não-oficial
4662/tcp	OrbitNet Message Service	Official
4664/tcp	Google Desktop Search	Não-oficial
4672/udp	eMule - port often used	Não-oficial
4894/tcp	LysKOM Protocol A	Official
4899/tcp	Radmin remote administration tool (program sometimes used as a Trojan horse)	Official
5000/tcp	commplex-main	Official
5000/tcp	UPnP - Windows network device interoperability	Não-oficial
5001/tcp	Slingbox and Slingplayer	Não-oficial
5003/tcp	FileMaker Filemaker Pro	Official
5004/udp	RTP Real-time Transport Protocol	Official
5005/udp	RTP Real-time Transport Protocol	Official
5050/tcp	Yahoo! Messenger Yahoo! Messenger	Official
5051/tcp	ita-agent Symantec Intruder Alert	Official
5060/tcp	Session Initiation Protocol (SIP)	Official
5060/udp	Session Initiation Protocol (SIP)	Official
5061/tcp	Session Initiation Protocol (SIP) over Transport Layer Security (TLS)	Official
5093/udp	SPSS License Administrator (SPSS)	Official
5104/tcp	IBM NetCOOL / IMPACT HTTP Service	Não-oficial
5121	Neverwinter Nights and its mods, such as Dungeon Eternal X	Não-oficial
5190/tcp	ICQ, AOL Instant Messenger e MSN Messenger	Official
5222/tcp	XMPP/Jabber - client connection	Official
5223/tcp	XMPP/Jabber - default port for SSL Client Connection	Não-oficial
5269/tcp	XMPP/Jabber - server connection	Official
5351/tcp,udp	NAT Port Mapping Protocol - client-requested configuration for inbound connections through network address translators	Official
5353/udp	mDNS - multicastDNS	
5402/tcp,udp	StarBurst AutoCast MFTP	Official
5405/tcp,udp	NetSupport Manager	Official
5432/tcp	PostgreSQL database system	Official
5445/udp	Cisco Vidéo VT Advantage	???
5495/tcp	Applix TM1 Admin server	Não-oficial
5498/tcp	Hotline tracker server connection	Não-oficial
5499/udp	Hotline tracker server discovery	Não-oficial
5500/tcp	VNC remote desktop protocol - for incoming listening viewer, Hotline control connection	Não-oficial
5501/tcp	Hotline file transfer connection	Não-oficial
5517/tcp	Setiqueue Proxy server client for SETI@Home project	Não-oficial
5555/tcp	Freeciv multiplay port for versions up to 2.0, Hewlett Packard Data Protector, SAP	Não-oficial
5556/tcp	Freeciv multiplay port	Official
5631/tcp	Symantec pcAnywhere	Official
5666/tcp	NRPE (Nagios)	Não-oficial
5667/tcp	NSCA (Nagios)	Não-oficial
5800/tcp	VNC remote desktop protocol - for use over HTTP	Não-oficial
5814/tcp,udp	Hewlett-Packard Support Automation (HP OpenView Self-Healing Services)	Official
5900/tcp	VNC remote desktop protocol (used by ARD)	Official
6000/tcp	X11 - used between an X client and server over the network	Official
6001/udp	X11 - used between an X client and server over the network	Official
6005/tcp	Default port for BMC Software CONTROL-M/Server - Socket Port number used for communication between CONTROL-M processes - though often changed during installation	Não-oficial
6050/tcp	Brightstor Arcserve Backup Exec	Não-oficial
6051/tcp	Brightstor Arcserve Backup Exec	Não-oficial
6112/tcp	"dtspcd" - a network daemon that accepts requests from clients to execute commands and launch applications remotely	Official
6112/tcp	Blizzard's Battle.net gaming service, ArenaNet gaming service	Não-oficial
6129/tcp	Dameware Remote Control	Não-oficial
6257/udp	WinMX (see also 6699)	Não-oficial
6346/tcp,udp	gnutella-svc (FrostWire, Limewire, Bearshare, etc.)	Official
6347/tcp,udp	gnutella-rtr	Official
6502/tcp,udp	Danware Data NetOp Remote Control	Não-oficial
6522/tcp	Gobby (and other libobby-based software)	Não-oficial
6543/udp	Jetnet - default port that the Paradigm Research & Development Jetnet protocol communicates on	Não-oficial
6566/tcp	SANE (Scanner Access Now Easy) - SANE network scanner daemon	Não-oficial
6619/tcp,udp	ODETTE-FTP over TLS/SSL	Official
6665-6669/tcp	Internet Relay Chat	Official
6679/tcp	IRC SSL (Secure Internet Relay Chat) - port often used	Não-oficial
6697/tcp	IRC SSL (Secure Internet Relay Chat) - port often used	Não-oficial
6699/tcp	WinMX (see also 6257)	Não-oficial
6881-6999/tcp,udp	BitTorrent full range of ports used most often	Não-oficial
6891-6900/tcp,udp	Windows Live Messenger (File transfer)	Official
6901/tcp,udp	Windows Live Messenger (Voice)	Official
6969/tcp	acmsoda	Official
6969/tcp	BitTorrent tracker port	Não-oficial
7000/tcp	Default port for Azureus's built in HTTPS Bittorrent Tracker	Não-oficial
7001/tcp	Default port for BEA WebLogic Server's HTTP server - though often changed during installation	Não-oficial
7002/tcp	Default port for BEA WebLogic Server's HTTPS server - though often changed during installation	Não-oficial
7005/tcp,udp	Default port for BMC Software CONTROL-M/Server and CONTROL-M/Agent's - Agent to Server port though often changed during installation	Não-oficial
7006/tcp,udp	Default port for BMC Software CONTROL-M/Server and CONTROL-M/Agent's - Server to Agent port though often changed during installation	Não-oficial
7010/tcp	Default port for Cisco AON AMC (AON Management Console) [6]	Não-oficial
7171/tcp	Tibia	
7312/udp	Sibelius License Server port	Não-oficial
7707/tcp	Default port used by Killing Floor game	Oficial
7777/tcp	Default port used by Windows backdoor program tini.exe	Não-oficial
7777/udp	SAMP	Não-oficial
8000/tcp	iRDMI - often mistakenly used instead of port 8080 (The Internet Assigned Numbers Authority (iana.org) officially lists this port for iRDMI protocol)	Official
8000/tcp	Common port used for internet radio streams such as those using SHOUTcast	Não-oficial
8002/tcp	Cisco Systems Unified Call Manager Intercluster Port
8008/tcp	HTTP Alternate	Official
8008/tcp	IBM HTTP Server default administration port	Não-oficial
8010/tcp	XMPP/Jabber File transfers	Não-oficial
8074/tcp	Gadu-Gadu	Não-oficial
8080/tcp	HTTP Alternate (http_alt) - commonly used for web proxy and caching server, or for running a web server as a non-root user	Official
8080/tcp	Jakarta Tomcat	Não-oficial
8086/tcp	HELM Web Host Automation Windows Control Panel	Não-oficial
8086/tcp	Kaspersky AV Control Center TCP Port	Não-oficial
8087/tcp	Hosting Accelerator Control Panel	Não-oficial
8087/udp	Kaspersky AV Control Center UDP Port	Não-oficial
8090/tcp	Another HTTP Alternate (http_alt_alt) - used as an alternative to port 8080	Não-oficial
8118/tcp	Privoxy web proxy - advertisements-filtering web proxy	Official
8087/tcp	SW Soft Plesk Control Panel	Não-oficial
8200/tcp	GoToMyPC	Não-oficial
8220/tcp	Bloomberg	Não-oficial
8222	VMware Server Management User Interface (insecure web interface)[2]. See also, port 8333	Não-oficial
8291/tcp	Winbox - Default port on a MikroTik RouterOS for a Windows application used to administer MikroTik RouterOS	Não-oficial
8294/tcp	Bloomberg	Não-oficial
8330	MultiBit HD, [7]	Não-oficial
8331	MultiBit, [8]	Não-oficial
8332	Bitcoin JSON-RPC server[3]	Não-oficial
8333	Bitcoin[4]	Não-oficial
8333	VMware Server Management User Interface (secure web interface)[2]. See also, port 8222	Não-oficial
8400	Commvault Unified Data Management[5].	Official
8443/tcp	SW Soft Plesk Control Panel	Não-oficial
8500/tcp	ColdFusion Macromedia/Adobe ColdFusion default Webserver port	Não-oficial
8767	TeamSpeak - Default UDP Port	Não-oficial
8880	WebSphere Application Server SOAP Connector port	
8888/tcp,udp	NewsEDGE server	Official
8888/tcp	Sun Answerbook dwhttpd server (deprecated by docs.sun.com)	Não-oficial
8888/tcp	GNUmp3d HTTP music streaming and web interface port	Não-oficial
9000/tcp	Buffalo LinkSystem web access	Não-oficial
9001	cisco-xremote router configuration	Não-oficial
9001	Tor network default port	Não-oficial
9009	Pichat Server - P2P chat software de servidor	Official
9043/tcp	WebSphere Application Server Administration Console secure port	
9060/tcp	WebSphere Application Server Administration Console	
9100/tcp	Jetdirect HP Print Services	Official
9101	Bacula Director	Official
9102	Bacula File Daemon	Official
9103	Bacula Storage Daemon	Official
9200/tcp	wap-wsp
9535/tcp	man, Remote Man Server	
9535	mngsuite - Management Suite Remote Control	Official
9800/tcp,udp	WebDav Source Port	Official
9800	WebCT e-learning portal	Não-oficial
9999	Hydranode - edonkey2000 telnet control port	Não-oficial
9999	Urchin Web Analytics	Não-oficial
10000	Webmin - web based Linux admin tool	Não-oficial
10000	BackupExec	Não-oficial
10008	Octopus Multiplexer - CROMP protocol primary port, hoople.org	Official
10050/tcp,udp	Zabbix-Agent	Official
10051/tcp,udp	Zabbix-Server	Official
10113/tcp	NetIQ Endpoint	Official
10113/udp	NetIQ Endpoint	Official
10114/tcp	NetIQ Qcheck	Official
10114/udp	NetIQ Qcheck	Official
10115/tcp	NetIQ Endpoint	Official
10115/udp	NetIQ Endpoint	Official
10116/tcp	NetIQ VoIP Assessor	Official
10116/udp	NetIQ VoIP Assessor	Official
10480	SWAT 4 Dedicated Server	Não-oficial
11235	Savage:Battle for Newerth Server Hosting	Não-oficial
11294	Blood Quest Online Server	Não-oficial
11371	OpenPGP HTTP Keyserver	Official
11576	IPStor Server management communication	Não-oficial
12345	NetBus - remote administration tool (often Trojan horse). Also used by NetBuster. Little Fighter 2 (TCP).	Não-oficial
12975/tcp	LogMeIn Hamachi (VPN tunnel software;also port 32976)
13720/tcp	Symantec NetBackup - bprd	
13721/tcp	Symantec NetBackup]] - bpdbm	
13724/tcp	Symantec Network Utility - vnet	
13782/tcp	Symantec NetBackup - bpcd	
13783/tcp	Symantec VOPIED protocol	
14567/udp	Battlefield 1942 e mods	Não-oficial
15000/tcp	Wesnoth
15567/udp	Battlefield Vietnam and mods	Não-oficial
15345/udp	XPilot	Official
16384/udp	Iron Mountain Digital - online backup	Não-oficial
16567/udp	Battlefield 2 and mods	Não-oficial
19226/tcp	Panda Software AdminSecure Communication Agent	Não-oficial
19813/tcp	4D database Client Server Communication	Não-oficial
20000	Usermin - web based user tool	Oficial
20720/tcp	Symantec i3 Web GUI server	Não-oficial
22347/tcp,udp	WibuKey - default port for WibuKey Network Server of WIBU-SYSTEMS AG	Oficial
22350/tcp,udp	CodeMeter - default port for CodeMeter Server of WIBU-SYSTEMS AG	Oficial
24800	Synergy: keyboard/mouse sharing software	Não-oficial
24842	StepMania: Online: Dance Dance Revolution Simulator	Não-oficial
25565/tcp,udp	Minecraft: Jogo Online	Não-oficial
25575/tcp,udp	Minecraft: Porta RCON - Jogo Online	Não-oficial
25999/tcp	Xfire	?
26000/tcp,udp	id Software's Quake server,	Oficial
26000/tcp	CCP's EVE Online Online gaming MMORPG,	Não-oficial
27000/udp	(through 27006) id Software's QuakeWorld master server	Não-oficial
27010	Half-Life and its mods, such as Counter-Strike	Não-oficial
27015	Half-Life and its mods, such as Counter-Strike	Não-oficial
27374	Sub7's default port. Most script kiddies do not change the default port.	Não-oficial
27500/udp	(through 27900) id Software's QuakeWorld	Não-oficial
27888/udp	Kaillera server	Não-oficial
27900	(through 27901) Nintendo Wi-Fi Connection	Não-oficial
27901/udp	(through 27910) id Software's Quake II master server	Não-oficial
27960/udp	(through 27969) Activision's Enemy Territory and id Software's Quake III Arena e Quake III	Não-oficial
28910	Nintendo Wi-Fi Connection	Não-oficial
28960	Call of Duty 2 Common Call of Duty 2 port - (PC Version)	Não-oficial
29900	(through 29901) Nintendo Wi-Fi Connection	Não-oficial
29920	Nintendo Wi-Fi Connection	Não-oficial
30000	Pokemon Netbattle	Não-oficial
30564/tcp	Multiplicity: keyboard/mouse/clipboard sharing software	Não-oficial
31337/tcp	Back Orifice - remote administration tool (often Trojan horse)	Não-oficial
31337/tcp	xc0r3 - xc0r3 security antivir port	Não-oficial
31415	ThoughtSignal - Server Communication Service (often Informational)	Não-oficial
31456-31458/tcp	TetriNET ports (in order: IRC, game, and spectating)	Não-oficial
32245/tcp	MMTSG-mutualed over MMT (encrypted transmission)	Não-oficial
32400	Plex Server	Não-oficial
33434	traceroute	Oficial
37777/tcp	Digital Video Recorder hardware	Não-oficial
36963	Counter Strike 2D porta multiplayer	Não-oficial
40000	SafetyNET p	Oficial
43594-43595/tcp	RuneScape	Não-oficial
47808	BACnet Building Automation and Control Networks	Oficial

\033[0;0m''')

