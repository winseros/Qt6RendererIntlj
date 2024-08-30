# QT6 Renderer Intellij Plugin

The plugin for pretty printing [Qt][qt] types by [CLion][clion] and other compatible Intellij IDEs.

> [!NOTE]
> The plugin wraps [Qt6Renderer][qt6renderer]. Bring up any problems there.

## Qt versions support
* 6.x

See the note about some problems with 6.4.2 and below.

## Qt types support
* [See here for gdb][qt6renderer_files_gdb]
* [See here for lldb][qt6renderer_files_lldb]

You can use the [example project][qt6renderer_exmpl] for testsing.

## Debuggers support
* LLDB
* GDB

## Operating systems tested on
* Windows
  * Bundled LLDB 9
  * Bundled GDB 13 
* Linux
  * Bundled LLDB 13
  * Bundled GDB 13

## Architectures tested on
* x64

## Requirements

See at the [Qt6Renderer](https://github.com/winseros/Qt6Renderer?tab=readme-ov-file#requirements).

## Troubleshooting

See at the [Qt6Renderer](https://github.com/winseros/Qt6Renderer?tab=readme-ov-file#troubleshooting).

[qt]: https://www.qt.io/
[clion]: https://www.jetbrains.com/clion/
[gdb]: https://sourceware.org/gdb/
[lldb]: https://lldb.llvm.org/
[qt6renderer]: https://github.com/winseros/Qt6Renderer
[qt6renderer_files_gdb]: https://github.com/winseros/Qt6Renderer/tree/master/python/gdb/qt6renderer
[qt6renderer_files_lldb]: https://github.com/winseros/Qt6Renderer/tree/master/python/lldb/qt6renderer
[qt6renderer_exmpl]: https://github.com/winseros/Qt6RendererExmpl
[qt6renderer_intlj]: https://github.com/winseros/Qt6RendererIntlj
[qt6renderer_vsc]: https://github.com/winseros/Qt6RendererVscj