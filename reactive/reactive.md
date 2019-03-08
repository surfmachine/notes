Reactive Programming
===============================================================================

[TOC]


-------------------------------------------------------------------------------
# ReactiveX

## Introduction
http://reactivex.io/intro.html

**Synonyms**

- Publisher / Subcriber 
- Source    / Sink

**Subscribe**
- onNext (0..n times)
- onCompleted or onError (1 time) 
 
**Unsubscribing**
- unsubscribe methode
- The results of this unsubscription will cascade back through the chain of operators that applies to theObservable that the observer subscribed to, and this will cause each link in the chain to stop emitting items

**Hot, Cold and Connectable Observers**
- A “hot” Observable may begin emitting items as soon as it is created, and so any observer who later subscribes to thatObservable may start observing the sequence somewhere in the middle. 

- A “cold” Observable, on theother hand, waits until an observer subscribes to it before it begins to emit items, and so such an observer isguaranteed to see the whole sequence from the beginning. 

- “Connectable”: In some implementations of ReactiveX, there is also something called a “Connectable” Observable.Such an Observable does not begin emitting items until its Connect method is called, whether or not anyobservers have subscribed to it. 

  
## Observable   

See:  http://reactivex.io/documentation/observable.html  

Categories:
- **Creation**
  Create, Defer, Empty/Never/Throw, From, Interval, Just, Range,Repeat, Start, Timer

- **Transformation**
  Buffer, FlatMap, GroupBy, Map, Scan, Window

- **Filtering**
  Debounce, Distinct, ElementAt, Filter, First, IgnoreElements, Last, Sample, Skip, SkipLast, Take, TakeLast

- **Combining Observables** 
  And/Then/When, CombineLast, Join, Merge, StartWith, Switch, Zip

- **Error Handling Operators** 
  Catch (revover from onError), Retry (resubscribe after onError)

- **Observable utitlity operators** 
  Delay, Do, Materialize/Dematerialize, ObserveOn, Serialize, Subscribe, SubscribeOn, TimeInterval, Timeout, Timestamp, Using

- **Conditional and boolean operators**
  All, Amb, Contains, DefaultIfEmpty, SequenceEqual, SkipUntil, SkipWhile, TakeUntil, TakeWhile 
  
- **Mathematical and aggregate operators**
  Average, Concat, Count, Max, Min, Reduce, Sum
  
- **Backpressure operators (see below)**
  Strategies for coping with Observables that produce items more rapidly than their observers consume them: http://reactivex.io/documentation/operators/backpressure.html

- **Connectable operators** 
  Connect, Publish, RefCount, Replay

- **Convertion**
  To (convert an Observable into another object or data structure)


## Single

See: http://reactivex.io/documentation/single.html

- RxJava (and its derivatives like RxGroovy & RxScala) has developed an Observable variant called “Single.” 

- A Single is something like an Observable, but instead of emitting a series of values — anywhere from noneat all to an infinite number — it always either emits one value or an error notification. 

Subscribe:
- onSuccess a Single passes this method the sole item that the Single emits
- onError   a Single passes this method the Throwable that caused the Single to be unable to emit an item

A Single will call only one of these methods, and will only call it once. Upon calling either method, theSingle terminates and the subscription to it ends. 

Composition via Single Operators:

operator     | returns      | description
------------ | ------------ | -------------------------------------------------
compose      | Single       | allows you create a custom operator 
concat       | Observable   | concatenates the items emitted by multiple Singles as Observable emissions 
concatWith   | Observable   | concatenates the items emitted by multiple Singles as Observable emissions 
create       | Single       | create a Single from scratch by calling subscriber methods explicitly 
delay        | Single       | move the emission of an item from a Single forward in time 
doOnError    | Single       | returns a Single that also calls a method you specify when it calls onError 
doOnSuccess  | Single       | returns a Single that also calls a method you specify when it calls onSuccess 
error        | Single       | returns a Single that immediately notifies subscribers of an error 
flatMap      | Single       | returns a Single that is the result of a function applied to an item emitted by a Single 
flatMapObservable |  Observable |  returns an Observable that is the result of a function applied to an item emitted by a Single 
from         | Single       | converts a Future into a Single 
just         | Single       | returns a Single that emits a specified item 
map          | Single       | returns a Single that emits the result of a function applied to the item emitted by the source Single 
merge        | Single       | converts a Single that emits a second Single into a Single that emits the item emitted by the second Single 
merge        | Observable   | merges the items emitted by multiple Singles as Observable emissions 
mergeWith    | Observable   | merges the items emitted by multiple Singles as Observable emissions 
observeOn    | Single       | instructs the Single to call the subscriber methods on a particular Scheduler 
onErrorReturn| Single       | converts a Single that makes an error notification into a Single that emits a specified item 
subscribeOn  | Single       | instructs the Single to operate on a particular Scheduler 
timeout      | Single       | returns a Single that makes an error notification if the source Single does not emit a value in a specified time period 
toSingle     | Single       | converts an Observable that emits a single item into a Single that emits that item 
toObservable | Observable   | converts a Single into an Observable that emits the item emitted by the Single and then completes 
zip, zipWith | Single       | returns a Single that emits an item that is the result of a function applied to items emitted by two or more other Singles 

## Subject

See: http://reactivex.io/documentation/subject.html

A Subject is a sort of bridge or proxy that is available in some implementations of ReactiveX that **acts both asan observer and as an Observable**.  Because it is an observer, 
- it can subscribe to one or more Observables, and because it is an Observable, 
- it can pass through the items it observes by reemitting them, and 
- it can also emitnew items. 


Varieties of Subject

- An **AsyncSubject** emits the last value (and only the last value) emitted by the source Observable,and only after that source Observable completes. (If the source Observable does not emit any values, the AsyncSubject also completes without emitting any values.) 

- When an observer subscribes to a **BehaviorSubject**, it begins by emitting the item most recentlyemitted by the source Observable (or a seed/default value if none has yet been emitted) and then continues toemit any other items emitted later by the source Observable(s). 

- **PublishSubject** emits to an observer only those items that are emitted by the source Observable(s)subsequent to the time of the subscription. 

  Note: 
  - That a PublishSubject may begin emitting items immediately upon creation (unless you havetaken steps to prevent this), and so there is a risk that one or more items may be lost between the time theSubject is created and the observer subscribes to it. 
  - If you need to guarantee delivery of all items from thesource Observable, you’ll need either to form that Observable with Create so that you can manually reintroduce “cold” Observablebehavior (checking to see that all observers have subscribed before beginning to emit items), or switch tousing a ReplaySubject instead. 

- **ReplaySubject** emits to any observer all of the items that were emitted by the sourceObservable(s), regardless of when the observer subscribes. 


## Scheduler 

See: http://reactivex.io/documentation/scheduler.html

Implementation Sample: 
Reactor and RxJava provide thread pool abstractions, called Schedulers, to use with the publishOn operator that is used to switch processing to a different thread pool. The schedulers have names that suggest a specific concurrency strategy — for example, “parallel” (for CPU-bound work with a limited number of threads) or “elastic” (for I/O-bound work with a large number of threads). If you see such threads, it means some code is using a specific thread pool Scheduler strategy.


## Implementing your own operators
See http://reactivex.io/documentation/implement-operator.html 


-------------------------------------------------------------------------------
# Reactive Streams

## Introduction
http://www.reactive-streams.org/ 

## The Reactive Streams initiative
The Reactive Streams initiative is an initiative to provide a standard for asynchronous stream processing with non-blocking back pressure. This standard is specified through the following interface:
- Processor<T,R> - This class represents a processing stage, which is both a Subscriber and a Publisher and obeys the contracts of both.
- Publisher<T> - This is a provider of a potentially unbounded number of sequenced elements, publishing them according to the demand received from its Subscribers.
- Subscriber<T> - Instances of this class will receive calls to Subscriber.onSubscribe(Subscription) once after passing an instance of Subscriber to Publisher.subscribe(Subscriber)
- Subscription - This class represents a one-to-one lifecycle of a Subscriber subscribing to a Publisher.

## Reactive Streams Data Flow
While dealing with reactive streams, the data flow as follows:
1. The subscribe method is called on a Publisher instance.
2. Then a Subscription object is created and the onSubscribe method of the Subscriber is executed with the Subscription object.
3. After that, a Subscriber will call the request method in the Subscription class to specify the number of objects it can process (If this method is not called explicitly, an unbounded number of objects is requested).
4. Then the Subscriber can receive objects via the onNext method. If the Subscriber receives all the objects it requested, it can request more object or cancel the Subscription by calling onComplete. If at some point there is an error the Publisher calls the onError method on the Subscriber.


-------------------------------------------------------------------------------
# JavaRx


## TODO Buch
- Flow, S.14/15


## TODO Reactive
- https://github.com/ReactiveX/RxJava/wiki/How-To-Use-RxJava 
- https://www.pluralsight.com/courses/reactive-programming-java-8-rxjava



-------------------------------------------------------------------------------
# Spring Webflux & Reactor

## Introduction

- Introduction to Spring WebFlux
  https://auth0.com/blog/introduction-getting-started-with-spring-webflux-api/
  Source Code
  https://github.com/auth0-blog/spring-webflux-oauth

- Spring Reactive Stack
  https://docs.spring.io/spring/docs/current/spring-framework-reference/web-reactive.html


### Spring WebFlux
To support reactive programming and the creation of reactive systems, the Spring Boot team created a whole new web stack called Spring WebFlux. 

This new web stack supports annotated controllers, functional endpoints, WebClient (analogous to RestTemplate in Spring Web MVC), WebSockets and a lot more.

### Reactor (Reactive Streams library)
Reactor is the reactive library of choice for Spring WebFlux. It provides the Mono and Flux API types to work on data sequences of 
- 0..1 (Mono) and 
- 0..N (Flux) 

through a rich set of operators aligned with the ReactiveX vocabulary of operators. Reactor is a Reactive Streams library and, therefore, all of its operators support non-blocking back pressure. Reactor has a strong focus on server-side Java. It is developed in close collaboration with Spring.

The implementations support operators like map, filter, reduce, and flatMap which maps every entry in a Publisher to another Publisher. Last but not least, in order to get data from a publisher(Flux or Mono) you need to call the subscribe on it.


## Sample

==TODO==
https://www.baeldung.com/spring-webflux
https://www.callicoder.com/reactive-rest-apis-spring-webflux-reactive-mongo/ 


-------------------------------------------------------------------------------
# References

- ReactiveX
  http://reactivex.io 

- Rx Workshop
  https://channel9.msdn.com/Series/Rx-Workshop/Rx-Workshop-Introduction 

- Introduction to Rx
  http://introtorx.com/ 

- "Reactive Streams in Java" Code Samples 
  https://github.com/Apress/reactive-streams-in-java  

- Tutorials
  http://reactivex.io/tutorials.html 

  Practical RxJava (cool Presentation)
  https://www.jfokus.se/jfokus16/preso/PracticalRxJava.pdf   


-------------------------------------------------------------------------------
_The end._

