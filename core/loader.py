import ctypes

from typing import Any


class Loader_x64():
    def __init__(self, dll_path: str) -> None:
        self.dll = ctypes.WinDLL(dll_path)

    """ DLL Injection Methods """

    def remote_process_inject(self, dll_path: bytes, pid: int) -> bool:
        # extern "C" INJECTLIB_API bool rmtdll(std::string dllPath, DWORD pid);
        self.dll.rmtdll.argtypes = [ctypes.c_char_p, ctypes.c_uint32]
        self.dll.rmtdll.restype = ctypes.c_bool
        return self.dll.rmtdll(dll_path, pid)

    def reflect_dll_inject(self, dll_path: bytes, pid: int) -> bool:
        # extern "C" INJECTLIB_API bool refdll(std::string dllPath, DWORD pid);
        self.dll.refdll.argtypes = [ctypes.c_char_p, ctypes.c_uint32]
        self.dll.refdll.restype = ctypes.c_bool
        return self.dll.refdll(dll_path, pid)

    def apc_dll_inject(self, dll_path: bytes, pid: int) -> bool:
        # extern "C" INJECTLIB_API bool apcdll(std::string dllPath, DWORD pid);
        self.dll.apcdll.argtypes = [ctypes.c_char_p, ctypes.c_uint32]
        self.dll.apcdll.restype = ctypes.c_bool
        return self.dll.apcdll(dll_path, pid)

    def net_dll_inject(self, dll_path: bytes, pid: int) -> bool:
        # extern "C" INJECTLIB_API bool net(std::string dllPath, DWORD pid);
        self.dll.net.argtypes = [ctypes.c_char_p, ctypes.c_uint32]
        self.dll.net.restype = ctypes.c_bool
        return self.dll.net(dll_path, pid)

    """ Shellcode Inject Methods """

    def remote_shellcode_inject(self, based_shellcode: bytes, pid: int) -> bool:
        # extern "C" INJECTLIB_API bool rmtsc(std::string shellcode, DWORD pid);
        self.dll.rmtsc.argtypes = [ctypes.c_char_p, ctypes.c_uint32]
        self.dll.rmtsc.restype = ctypes.c_bool
        return self.dll.rmtsc(based_shellcode, pid)

    def apc_shellcode_inject(self, based_shellcode: bytes, pid: int) -> bool:
        # extern "C" INJECTLIB_API bool apcsc(std::string shellcode, DWORD pid);
        self.dll.apcsc.argtypes = [ctypes.c_char_p, ctypes.c_uint32]
        self.dll.apcsc.restype = ctypes.c_bool
        return self.dll.apcsc(based_shellcode, pid)

    def context_shellcode_inject(self, based_shellcode: bytes, pid: int) -> bool:
        # extern "C" INJECTLIB_API bool ctxsc(std::string shellcode, DWORD pid);
        self.dll.ctxsc.argtypes = [ctypes.c_char_p, ctypes.c_uint32]
        self.dll.ctxsc.restype = ctypes.c_bool
        return self.dll.ctxsc(based_shellcode, pid)

    """ Auxliary Methods """

    def get_pid_by_name(self, process_name: bytes) -> int:
        self.dll.getPID.argtypes = [ctypes.c_char_p]     # 参数是 const char*
        self.dll.getPID.restype = ctypes.c_uint32        # 返回 DWORD（uint32）
        return self.dll.getPID(process_name)
