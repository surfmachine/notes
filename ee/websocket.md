WebSocket
===============================================================================


[TOC]

-------------------------------------------------------------------------------
# Einführung

## Standard
- WebSocket ist ein Standdard der Internet Engineering Task Force (IETF)
- Der Standard ist im Request for Comment (RFC) 6455 definiert
- Das WebSocket Protokoll arbeitet "on top of" TCP und wird für die Kommunikation zwischen HTTP Clienst und Server verwendet
- Hierzu kann der Client beim initialen Handshake via HTTP Upgrade machanismus den Server anfragen, das Protokoll zu wechseln.
- Sobald eine WebSocket Verbindung hergestellt wurde, bleibt die "darunterliegende" TCP Verbindung bestehen

## Beispiel HTTP Upgrade Handshake
Handshake Client Anfrage:
```
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Origin: http://example.com
Sec-WebSocket-Protocol: chat, superchat
Sec-WebSocket-Version: 13
```

Handshake Server Antwort:
```
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
Sec-WebSocket-Protocol: chat
```

## Features
- Eine WebSocket Session ist Bi-direktional und full-duplex
- Sobald die WebSocket Session steht, können Server und Client unabhängig von einander Meldungen senden
- Damit bieten WebSockets eine ideale Lösung für Anwendungen mit häufigen Meldungen und kurzen Wartezeiten wie zum Beispiel Online Games oder Broadcasting von Real Time Daten
- Verglichen mit bisherigen Lösungsansätzen wie Long Polling verursachen WebSockets daher HTTP Aufrufe, sind effizienter und bieten mehr Möglichkeiten


-------------------------------------------------------------------------------
# Java

## Overview

### Java WebSocket API
- Die Java WebSocket API ist im JSR 356 spezifiert und seit 2013 verfügbar
- Die Referenzimplementation ist das Open Source Projekt Tyrus
- Seit Java EE 7 ist WebSocket auch Bestandteil der Enterprise Edition
- Jeder Java EE kompatible Server beinhaltet eine default Implenentation wie zum Beispiel:
  - Tyrus bei WebLogic und Glassfish
  - Untertow bei JBoss EAP und Wildfly
  - Interne Implementation bei Tomcat (ab Version 7)
- Die API beinhaltet sowohl Komponente für die Erstellung eines WebSocket Server als auch eines WebSoccket Clients
- Siehe auf Grafik unter [Oracle Intro]
- Das Package javax.websocket enhält die Client APIs und alle gemeinsamen (Client und Server) Klassen
- Das Package javax.websocket.server enthält alle Server spezifischen Klassen


### Container
- WebSocketContainer
  Provides a high level view of the container, allows client endpoint activation and connection to an existing (WebSocket) server, enforce global/common properties (idle connection timeout, message size, asynchronous send timeout) relevant to all endpoints
- ServerContainer
  Server side derivative of the WebSocketContainer which allows programmatic deployment of WebSocket endpoints
- ContainerProvider
  Provides access to an instance of the underlying WebSocketContainer


### Endpoint Configuration
- Es gibt zwei Arten Client oder Server Endpoints zu definieren:
  - Deklarativ mit Hilfe der Annotationen @ServerEndpoint und  @ClientEndpoint
  - Programmatisch durch Erweiterung der Klasse javax.websocket.Endpoint
- Bei deklarativen Ansatz werden folgenden Annoationen eingesetzt

Annotation      | Beschreibung
--------------- | ---------------------------------------------------------------
@ServerEndpoint | If decorated with @ServerEndpoint, the container ensures availability of the class as a WebSocket server listening to a specific URI space
@ClientEndpoint | A class decorated with this annotation is treated as a WebSocket client
@OnOpen         | A Java method with @OnOpen is invoked by the container when a new WebSocket connection is initiated
@OnMessage      | A Java method, annotated with @OnMessage, receives the information from the WebSocket container when a message is sent to the endpoint
@OnError        | A method with @OnError is invoked when there is a problem with the communication
@OnClose        | Used to decorate a Java method that is called by the container when the WebSocket connection closes



## Meldungstypen und Encoder/Decoder

### Meldungstypen
- Die WebSocket Spezfikation untertützt zwei Formate: text und binary
- Die Java WebSocket API untersützt zusätzlich Java Objekte und Ping/Pong Meldungen (für Health Checks)

Meldungstyp   | Beschreibung
------------- | ---------------------------------------------------------------
Text          | Textdaten (java.lang.String, primitive Datentypen und Wrapper)
Binary 	      | Binäre Daten wie audio, image, etc. (byte[], java.nio.ByteBuffer)
Java objects 	| Java Objekte die mit Hilfe von Encodern und Decodern in die Standard WebSocket Formate text oder binary konvertiert werden.
Ping, Pong    | Health Check Meldungen (javax.websocket.PongMessage ist die Antwort eines WebSocket Peer auf eine Ping Meldung)



## Weiteres
- Asynchrone Kommunikation
- Pfad Annotationen


-------------------------------------------------------------------------------
# Referenzen

## Dokumentation

- IETF
  https://www.ietf.org/

- RFC6455
  https://tools.ietf.org/html/rfc6455

- Java Specification Request (JSR 356)
  https://jcp.org/en/jsr/detail?id=356

- Java Reference Implementation (Tyrus)
  https://github.com/tyrus-project/tyrus

- Oracle Intro (Grafik)
  http://www.oracle.com/technetwork/articles/java/jsr356-1937161.html

- Java WebSocket API Handbook
  https://www.gitbook.com/book/abhirockzz/java-websocket-api-handbook/details

## Beispiele

- Basic Intro (einfacher Endpoint mit Encoder / Decoder)
  http://www.baeldung.com/java-websockets

- Oracle Sample with NetBeans
  http://www.oracle.com/webfolder/technetwork/tutorials/obe/java/HomeWebsocket/WebsocketHome.html

- Mozilla Sample, writing a WebSocket Server in Java
  https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_a_WebSocket_server_in_Java



_The end._
