# Python-Rust-Interoperability
How to use Rust library in Python

## Test 1. Pure Python: `/python`

```bash
$ cd python
$ python monte_carlo_pi.py
```

You have two calculation options:
1. CalcOption.MULTITHREADING: using Multi-threading
2. CalcOption.MULTIPROCESSING: using Multi-processing

```python
if __name__ == "__main__":
    calc_option = CalcOption.MULTITHREADING
```

## Test 2. Pure Rust: `/rust/monte_carlo_pi`

```bash
$ cd rust/py_monte_carlo_pi
```

The first experiment is to run `example` pi with `debug` mode.

```bash
$ cargo run --example pi
```

This is a little bit slow, whose performance can be improved with running `release` mode.

```bash
$ cargo run --example pi --release
```

## Test 3. Rust-Python Interoperability: `/rust/py_monte_carlo_pi`

```bash
$ cd /rust/py_monte_carlo_pi
$ cargo build --release
$ cp target/release/libmontecarlopi.dylib montecarlopi.so
$ pyhon main.py
```

## Test 4. Rust-Python Interoperability: `/rust/pyo3_monte_carlo_pi`

Using [pyo3](https://pyo3.rs/v0.17.3/).

```bash
$ cd /rust/pyo3_monte_carlo_pi
$ cargo build --release
$ cp target/release/libmontecarlopi.dylib montecarlopi.so
$ pyhon main.py
```
