from __future__ import annotations
import typing

__all__ = ["XCLBin"]

class XCLBin:
    def __init__(
        self, xclbin_path: str, kernel_name: str, device_index: int = 0
    ) -> None: ...
    def _get_buffer_host_address(self, arg0: int) -> int: ...
    def _run_only_npu_instructions(self) -> None: ...
    def load_npu_instructions(self, insts: list[int]) -> None: ...
    def mmap_buffers(
        self, shapes: list[list[int]], np_format: typing.Any
    ) -> list[memoryview]: ...
    def run(self) -> None: ...
    def sync_buffers_from_device(self) -> None: ...
    def sync_buffers_to_device(self) -> None: ...
    def wait(self, timeout: int | None = None) -> None: ...