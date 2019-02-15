Reactive Programming
===============================================================================

[TOC]


-------------------------------------------------------------------------------
# ReactiveX

## Introduction

See: http://reactivex.io/intro.html

Subscribe:
- onNext (0..n times)
- onCompleted or onError (1 time) 
 
Unsubscribing:
- unsubscribe methode
- The results of this unsubscription will cascade back through the chain of operators that applies to theObservable that the observer subscribed to, and this will cause each link in the chain to stop emitting items


Hot, Cold and Connectable Observers:
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




## Misc

- Implementing your own operators
  http://reactivex.io/documentation/implement-operator.html 


-------------------------------------------------------------------------------
# JavaRx

==TODO==
- https://github.com/ReactiveX/RxJava/wiki/How-To-Use-RxJava 
- https://www.pluralsight.com/courses/reactive-programming-java-8-rxjava


-------------------------------------------------------------------------------
# References

- ReactiveX
  http://reactivex.io 

- Rx Workshop
  https://channel9.msdn.com/Series/Rx-Workshop/Rx-Workshop-Introduction 

- Introduction to Rx
  http://introtorx.com/ 

- Tutorials
  http://reactivex.io/tutorials.html 


-------------------------------------------------------------------------------
_The end._

