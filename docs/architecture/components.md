# C4 Level 3: Components

!!! note "Write this lazily"
    There is no component doc yet, and that is correct. Write an L3 page for a
    container **only when** [Level 2's](containers.md) one paragraph about it
    stops being enough, or when someone is about to own or substantially change
    it. Writing all component docs up front is big-design-up-front; it produces
    pages that rot before anyone reads them.

When you do write one, it should cover, for a single container:

- The components inside it and each one's responsibility.
- How they collaborate (a mermaid component or sequence diagram).
- The internal contracts, linking to [interfaces](interfaces.md).

## Level 4 (code) is deliberately absent

Class-level diagrams change at code-speed and add little over reading the code.
Do not hand-maintain them. If you ever need one, generate it from the source and
throw it away.
