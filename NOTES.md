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


