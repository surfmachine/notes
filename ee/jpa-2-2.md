What's New in JPA 2.2
===============================================================================

[TOC]

-------------------------------------------------------------------------------
# Java 8 Date and Time Support

Ab JPA 2.2 werden folgende Typen des Date and Time API untersützt:
- java.time.LocalDate
- java.time.LocalTime
- java.time.LocalDateTime
- java.time.OffsetTime
- java.time.OffsetDateTime

Bis und mit JPA 2.1 hat JPA nur älterer Typen wie z.B. java.util.Date oder java.sql.Timestamp unterstützt. Um mit den neuen Typen arbeiten zu können musste man einen Konverter einsetzten.

Dies ist nicht mehr notwendig. Date and Time API Typen können direkt verwendet werden, wie das folgende Beispiel zeigt:
```
public class Job implements Serializable {

  @Column(name = "WORK_DATE")
  private LocalDate workDate;

  ...
}
```

Auch die Angabe von @Temporal (wie dies bei java.util.Date und java.util.Calendar notwendig war) entfällt.

Da mit JPA 2.2 nur ein Subset der Date and Time  API Typen unterstützt wird, kann es Fälle geben in denen weiterhin ein Konverter benötigt wird. Auch hier gibt es seit JPA 2.2 neue Möglichkeiten, wie die folgenden Beispiele zeigen.


-------------------------------------------------------------------------------
# Attribute Converter

## Attribute Converter erstellen
Das folgende Beispiel zeigt einen Converter für LocalDateTime und ZonedDateTime:
```
@Converter
public class LocalToZonedConverter
  implements AttributeConverter<ZonedDateTime, LocalDateTime> {

  @Override
  public LocalDateTime convertToDatabaseColumn (ZonedDateTime entityValue) {
    return entityValue.toLocalDateTime();
  }

  @Override
  public ZonedDateTime convertToEntityAttribute(LocalDateTime databaseValue) {
    return ZonedDateTime.of(databaseValue,ZoneId.systemDefault());
  }

}
```

## Attribute Converter anwenden
Damit der Converter zur Anwendung kommt, gibt es mehrere Varianten:
- Automatische Verwendung des Konverter bei allen Feldern mit dem entsprechenden Datentyp
- Anwendung des Converter für alle Attribute einer Klasse mit dem entsprechenden Datentyp
- Anwendung des Converter für einzelne Attribute

Automatische Verendung des Konverter bei allen Feldern mit dem entsprechenden Datentyp:
```
@Converter (autoApply=true)
public class LocalToZonedConverter ...
```

Anwendung des Converter für alle Attribute einer Klasse mit dem entsprechenden Datentyp:
```
@Convert(attributeName="workDate", converter = LocalDateConverter.class)
public class Job implements Serializable {
  ...
}
```

Angabe für einzelne Attribute:
```
  @Convert(converter=LocalDateConverter.java)
  private LocalDate workDate;
```

## Injectable Attribute Converter
Attribute Converter sind neu injectable, dass heisst es ist auch möglich, CDI beans in einen Converter injizieren zu lassen:
```
@Converter
public class CreditLimitConverter
  implements AttributeConverter<BigDecimal, BigDecimal> {

  @Inject
  CreditLimitEncryptor encryptor;

  @Override
  public BigDecimal convertToDatabaseColumn(BigDecimal entityValue) {
    String encryptedFormat = encryptor.base64encode(entityValue.toString());
    return BigDecimal.valueOf(Long.valueOf(encryptedFormat));
  }

  ...
}
```


-------------------------------------------------------------------------------
# Streaming Results of Query Executions

## Java Stream Feature
- JPA kann nun bei Resultaten von Abfragen mit den Java SE 8 Stream Features arbeiten
- Streams sind vielfach einfacher zum lesen und schreiben.
- Je nach Situation verhalten sich die Queries auch performanter beim Einsatz mit Streams
- Es gibt aber auch Fälle bei denen die ResultSet Pagination Funktion performanter ist als die Verwendung von Streams!
- Das neue Feature kann mit Hilfe der Methode getResultStream() genutzt werden, welche zu den Klassen Query und TypedQuery hinzugefügt wurde
- Damit gibt JPA einen Stream anstelle einer Liste zurück.
- Die Stream Implementation liest alle records auf einmal, daher ist bei grossen Datenmengen zu prüfen ob die scrollable ResultSet oder die Pagination Funktion nicht besser sind.


## Beispiel mit Ausgabe auf die Console
```
public void findByCustomer(PoolCustomer customer) {

  Stream<Job> jobList = em
    .createQuery("select object(o) from Job o where o.customer=:customer")
    .setParameter("customer", customer)
    .getResultStream();

  jobList.map(j -> j.getCustId() + ", id:" + j.getId() + "starts:" + j.getDate())
    .forEach(jm -> System.out.println(jm));

}
```

## Beispiel mit Rückgabe einer Liste
```
public List<Job> findByCustomer(PoolCustomer customer) {

  Stream<Job> jobList = em
    .createQuery("select object(o) from Job o where o.customer=:customer")
    .setParameter("customer", customer)
    .getResultStream();

    return jobList.collect(Collectors.toList());
}
```


## Beispiel mit zusätzlicher Filerung auf Shape
```
public List<Job> findByCustPoolShape (String poolShape) {

  Stream<Job> jobstream = em
    .createQuery("select object(o) from Job o")
    .getResultStream();

    return jobstream
      .filter(c -> poolShape.equals(c.getCustomerId().getPoolId().getShape()))
      .collect(Collectors.toList());
}
```


-------------------------------------------------------------------------------
# Repeatable Annotation Support

Seit Java SE 8 ist es möglich die gleiche Annotation mehrfach aufzuführen, ohne diese in eine "Container Annotation" zu hüllen.

Dazu gibt es eigens die @Repeatable Meta Annotation um bei der Definition einer Annotation anzugeben, dass diese mehrfach (auf dem gleichen Element) genutzt werden kann.

Ziel ist ein weitere Vereinfachung und mehr Übersichtlichkeit des Codes.

Beispiel mit Container Annotation:
```
@Entity
@NamedQueries({
  @NamedQuery(name="Customer.findAll", query="SELECT c FROM Customer c"),
  @NamedQuery(name="Customer.findById",query="SELECT c FROM Customer c ..."),
  @NamedQuery(name="Customer.findByName", query="SELECT ... "),
})
public class Customer implements Serializable {
  ...
}
```

Beispiel mit mehrfach Repetion:
```
@Entity
@NamedQuery(name="Customer.findAll", query="SELECT c FROM Customer c")
@NamedQuery(name="Customer.findById",query="SELECT c FROM Customer c ...")
@NamedQuery(name="Customer.findByName", query="SELECT ... ")
public class Customer implements Serializable {
  ...
}
```

-------------------------------------------------------------------------------
# Fazit
- JPA 2.2 enthält nicht eine Vielzahl von neuen Features.
- Die Erweiterungen und vor allem die Adaption an Java SE 8 sind aber sehr praktisch und führen zu einer weiteren Vereinfachung des Codes.
- Auch die Adaption mit CDI mmit der Möglichkeit, innerhalb von Attriubte Konvertern CDI Beans injizieren zu lassen ist sehr praktisch .
- JPA 2.2 ist Bestandteil von Java EE 8 und seit Q4/2017 verfügbar.

_The end._
