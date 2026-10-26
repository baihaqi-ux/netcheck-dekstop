import socket
import time


def measure_ping(host="8.8.8.8", port=53, count=5, timeout=2):
    """Ukur latency dengan menghitung waktu koneksi TCP ke server DNS Google.

    Return (rata-rata ms, jitter ms), atau None kalau semua percobaan gagal.
    """
    times = []
    for _ in range(count):
        start = time.perf_counter()
        try:
            with socket.create_connection((host, port), timeout=timeout):
                pass
            times.append((time.perf_counter() - start) * 1000)
        except OSError:
            pass
        time.sleep(0.2)

    if not times:
        return None

    rata_rata = sum(times) / len(times)

    # Jitter = rata-rata selisih antar pengukuran berurutan
    selisih = [abs(times[i] - times[i - 1]) for i in range(1, len(times))]
    jitter = sum(selisih) / len(selisih) if selisih else 0.0

    return rata_rata, jitter