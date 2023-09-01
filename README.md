# Concurrent Matrix Multiplication

This project implements a high-performance matrix multiplication tool in Rust by leveraging concurrency and parallelism. It can calculate the product of two matrices with arbitrary dimensions.

## Functionality

  Accepts two matrices of any size as input
    Spawns a thread pool to perform concurrent multiplication
    Divides each matrix into smaller blocks
    Each thread multiplies a block from matrix A with a block from matrix B
    Accumulates the partial results into the final output matrix
    Matrix blocking and threading improves CPU utilization

## Implementation

  Built using Rust and its native threads and synchronization primitives
    Creates a fixed size thread pool on startup
    Blocks input matrices into smaller sub-matrices based on number of threads
    Each thread picks up a block-wise multiplication job from a queue
    Results are placed in the output matrix through synchronized access

## Performance

  Concurrent design exploits parallelism in multi-core CPUs
    Matrix blocking improves cache utilization compared to naive multiplication
    Achieves near linear speedup with increase in number of threads
    Significantly faster than single-threaded implementation, This tool shows the performance benefits of concurrency and matrix decomposition for parallel workloads like matrix math. The project can be enhanced by exploring GPU computation and SIMD optimizations.
