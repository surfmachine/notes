Markdown template
===============================================================================

[TOC]


-------------------------------------------------------------------------------
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6

-------------------------------------------------------------------------------
# Next Header 1
## Next Header 2
### Next Header 3

-------------------------------------------------------------------------------
# Text 

Text:
*This text will be italic*
_This will also be italic_

**This text will be bold**
__This will also be bold__

_You **can** combine them_

~~This text will be strikethrough~~


Inline Code:
`<addr>` element here instead.


Block Quoate:
> We're living the future so
> the present is our past.


Mark:
==marked==


Superscript:
30^th^


Subscript:
H~2~O


Abbreviation:
*[HTML]: Hyper Text Markup Language
*[W3C]:  World Wide Web Consortium

The HTML specification is maintained by the W3C.


-------------------------------------------------------------------------------
# List

Simple List:
- Item A
- Item B
- Item C

Nested List:
- Item A
  - Item A.A
  - Item A.B
  - Item A.B
- Item B
- Item C

Numbered List:
1. hello 
2. tom 

Task List:
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item


-------------------------------------------------------------------------------
# Table


STATUS | BESCHREIBUNG
------ | --------------------------------------------------
  0    | INITIAL
  1    | REWORKED
  2    | DELIVERED



-------------------------------------------------------------------------------
# Source

Java:
```java
private String hello = "Hello Markdown";
System.out.println(hello);
```

JavaScript:
```javascript {.class1 .class}
function add(x, y) {
  return x + y
}
```

JavaScript with line numbers:
```javascript {.line-numbers}
function add(x, y) {
  return x + y
}
```

-------------------------------------------------------------------------------
# Link and Images:

- http://github.com
- [GitHub](http://github.com)


![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)


-------------------------------------------------------------------------------
# References 

- Mastering Markdown
  https://guides.github.com/features/mastering-markdown/#syntax
  
- Markdonw Basics
  https://shd101wyy.github.io/markdown-preview-enhanced/#/markdown-basics 

- Markdown Preview Enhanced Plugin (Visual Studio Code)
  https://shd101wyy.github.io/markdown-preview-enhanced/#/


-------------------------------------------------------------------------------
_The end._

