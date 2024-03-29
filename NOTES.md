SRP(Single  Responsibility Principle) or SOC(Separation of concerns)

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


## Command Query Separation

Command = asking for an action or change(e.g, please set your attack value to 2)
Query = asking for information (e.g, please give me your attack value)
CQS = having separate means of sending commands and queries to e.g, direct field access


# Command

An object which represents an instruction to perform a particular action.Contains all the information necessary for the action to be taken.

# Interpreter

A component that processes structured text data. Does so by turning it into separate lexical tokens(lexing) and then interpreting sequences of said tokens(parsing)

# Mediator

A component that facilitates communication between other components without them necessarily being aware of eache other or having direct(reference) access to each other.


# Memento

A token/handle representing the system state. Lets us roll back to the state when the token was generated May or may not directly expose state information

# Observer

An observer is an object that wishes to be informed about events happening in the system. The entity generating the events is an observable

# State

A pattern in which the object's behavior is determined by its state. An object transition from one state to another(something needs to trigger a translation)

A formalized construct which manages state and transitions is called state machine.


# Strategy

Enables the exact behavior of a system to be selected at run-time

# Template 

Allows us to define the 'skeleton' of the algorithm, with concrete implementations defined in subclasses


# Visitor

A component(visitor) that knows how to traverse a data structure compose of(possibly related)types.

