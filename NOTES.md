SRP(Single  Responsibility Priciple) or SOC(Separation of concerns)

# Gamma Categorization

+ Design Patterns are typically split into three categories
+ This is called Gamma Categorization after Erich Gamma, one of GoF authors
+ Creational Patterns
  + Deal with the creation(construction) of objects
  + Explicit(constructor) vs implicit(DI, reflection, etc)
  + Wholesale(single statement) vs . piecewise(step-by-step)
+ Structural Patterns
  + Concerned with the structure(e.g, class members)
  + Many patterns are wrappers that mimic the underlying class interface
  + Stress the importance of good API design
+ Behavior Patterns
  + The are all different; no central theme

## Builder

> When piecewise object construction is complicated, provide an API for doing it succinctly

## Prototype

> A partially or fully initialized object that you copy (clone) and make use of it.

# Bridge

> A mechanism that decouples an interface(hierarchy) from an implementation(hierarchy).

# facade

> Provide a simple, easy to understand/user interface over a large and sophisticated body of code

# flyweight

> A space optimization technique that lets us use less memory by storing externally the data associated with similar objects

# Proxy

> A class that functions as an interface to a particular resources. That resource may be remote, expensive to construct, or may requre logging or some other added functionality.


## Proxy vs . Decorator

+ Proxy provides an identical interface; decorator provides an enhanced interface
+ Decorator typically aggregates (or has reference to) what it is decorating; proxy doesn't have to
+ Proxy might not even be working with a materialized object

# Chain of Responsibility

> A chain of components who all get a chance to process a command on a query.optionally having default processing implementation and an ability to terminate the processing chain.


