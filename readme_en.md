![](https://img.shields.io/badge/joe1sn-S_inject-green)  ![](https://img.shields.io/badge/windows-C++-yellow)[中文](./readme.md)

<h1><p align="center">inject-mcp</p></h1>

<p align="center">Using MCP to complete DLL and Shellcode injection</p>

<p align="center"><img src="./README.assets/image-20240205141410967.png"></p>

Use the DLL version of the [S-inject](https://github.com/Joe1sn/S-inject) project as the core functionality implementation. For the special DLL format, please refer to the S-inject project. The project's `Test Files` also include some test files.

**Disclaimer:** This tool is intended solely for educational and authorized testing purposes. The developers and contributors do not support, encourage, or endorse any illegal or unauthorized use. Users are responsible for ensuring that their use of this tool complies with all applicable laws and regulations. Any unauthorized use of this tool is strictly prohibited. The developers and contributors shall not be held liable for any damages or consequences resulting from the use of this tool. Use it at your own risk. By using this tool, you agree to these terms and assume full responsibility for your actions.

# Install

Just like other MCP

```json
{
  "name": "inject-mcp",
  "key": "injectMCP",
  "command": "uv",
  "args": [
    "--directory",
    "D:\\Github\\inject-mcp",
    "run",
    "main.py"
  ]
}
```

- **--directory**：your local project path

# Demo

```
Use the AI tool inject to inject the local DLL into the process named x64dbg using the CreateRemoteThread method: D:\Github\S-inject\Test Files\TestDll_x64.dll
```

```
Use the AI tool inject to inject Shellcode into the process named x64dbg using the remote thread method: SDH/SPfnZUiLWGBIi1sYSItbIEiLG0iLG0iLWyBJidiLWzxMAcNIMclmgcH/iEjB6QiLFAtMAcJNMdJEi1IcTQHCTTHbRItaIE0Bw00x5ESLYiRNAcTrMltZSDHASIniUUiLDCRIMf9BizyDTAHHSInW86Z0BUj/wOvmWWZBiwREQYsEgkwBwFPDSDHJgMEHSLgPqJaRuoeanEj30EjB6AhQUeiw////SYnGSDHJSPfhUEi4nJ6TnNGah5pI99BQSInhSP/CSIPsIEH/1g==
```

![image-20250406152838520](D:\Github\inject-mcp\assets\image-20250406152838520.png)

https://github.com/user-attachments/assets/65ed3373-a187-4dd5-a807-425dca1d8ee9

# TODO

- [ ] FIX: 加载网络中的DLL失效
- [ ] Feat: 32位注入支持
- [ ] Feat: 自动分别32/64位后，自动注入