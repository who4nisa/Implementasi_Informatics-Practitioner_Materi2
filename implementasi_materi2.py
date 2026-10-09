import numpy as np
import pandas as pd
import time

print("==================================================================")
print(" STUDI KASUS KOMPREHENSIF: SIMULASI EVAKUASI BENCANA BERBASIS HPC")
print(" Berdasarkan Materi: Asst. Prof. Dr. Warawan Diaz Carbalo")
print(" Topik: Bridging Global Infrastructure to Address Local Challenges")
print("==================================================================\n")

# ==================================================================
# 1. KELAS AGEN & LINGKUNGAN (Agent-Based Simulation Architecture)
# ==================================================================
class EvacuationEnvironment:
    def __init__(self, width=200, height=200):
        self.width = width
        self.height = height
        # Titik kumpul aman (Assembly Point / Zona Evakuasi Utama)
        self.safe_zones = np.array([
            [180.0, 180.0],
            [180.0, 20.0]
        ])
        # Titik rawan bencana (misal: aliran sungai / zona rendah)
        self.hazard_zones = np.array([
            [50.0, 50.0],
            [60.0, 50.0]
        ])

class CrowdAgentSystem:
    def __init__(self, n_agents=500, env=None):
        self.n_agents = n_agents
        self.env = env
        
        # Inisialisasi posisi awal agen secara acak di area kampus/kota
        np.random.seed(42)
        self.positions = np.random.uniform(10, 100, size=(n_agents, 2))
        
        # Kecepatan acak tiap individu (m/s) merepresentasikan variasi fisik manusia
        self.speeds = np.random.normal(loc=2.5, scale=0.5, size=n_agents)
        self.speeds = np.clip(self.speeds, 1.0, 4.0)
        
        # Status agen: 0 = Belum Evakuasi, 1 = Aman (Evakuasi Sukses), -1 = Terjebak
        self.status = np.zeros(n_agents, dtype=int)
        
    def step_simulation(self):
        """
        Fungsi iterasi paralel untuk memperbarui posisi seluruh agen 
        menuju titik kumpul aman terdekat.
        """
        active_indices = np.where(self.status == 0)[0]
        if len(active_indices) == 0:
            return True # Semua selesai
            
        for i in active_indices:
            pos = self.positions[i]
            
            # Cari titik aman (safe zone) terdekat bagi agen ke-i
            distances = np.linalg.norm(self.env.safe_zones - pos, axis=1)
            target_zone = self.env.safe_zones[np.argmin(distances)]
            
            # Hitung arah vektor perpindahan (steering vector)
            to_target = target_zone - pos
            dist_to_target = np.linalg.norm(to_target)
            
            if dist_to_target < 3.0:
                self.status[i] = 1
                continue
                
            direction = to_target / dist_to_target
            
            # Faktor hambatan lingkungan & kepanikan (stochastic noise)
            panic_noise = np.random.normal(0, 0.8, size=2)
            
            # Update posisi baru berdasarkan kecepatan individu
            new_pos = pos + (direction * self.speeds[i]) + panic_noise
            
            # Batasi agar tidak keluar dari batas wilayah peta lingkungan
            new_pos[0] = np.clip(new_pos[0], 0, self.env.width)
            new_pos[1] = np.clip(new_pos[1], 0, self.env.height)
            
            self.positions[i] = new_pos
            
        return False

# ==================================================================
# 2. EKSEKUSI UTAMA & LOGGING ANALITIK (Simulasi HPC Workload)
# ==================================================================
print("--- [Inisialisasi Sistem Komputasi Simulasi] ---")
env = EvacuationEnvironment(width=200, height=200)

TOTAL_AGENTS = 1000
MAX_TIMESTEPS = 300

print(f"Total Agen Kerumunan : {TOTAL_AGENTS} Orang")
print(f"Batas Maksimal Waktu : {MAX_TIMESTEPS} Timestep")
print(f"Infrastruktur Target : Simulasi Paralel Berbasis Cluster / Lokal\n")

system = CrowdAgentSystem(n_agents=TOTAL_AGENTS, env=env)

print("--- [Memulai Eksekusi Iterasi Simulasi Evakuasi] ---")
start_time = time.time()

log_history = []

for t in range(MAX_TIMESTEPS):
    is_finished = system.step_simulation()
    
    succesful = np.sum(system.status == 1)
    trapped = np.sum(system.status == -1)
    pending = np.sum(system.status == 0)
    
    log_history.append({
        'timestep': t + 1,
        'sukses_evakuasi': succesful,
        'dalam_perjalanan': pending,
        'terjebak': trapped
    })
    
    if (t + 1) % 50 == 0 or is_finished:
        print(f"Timestep [{t + 1}/{MAX_TIMESTEPS}] -> Aman: {succesful}, Dalam Perjalanan: {pending}")
        
    if is_finished:
        print(f"\n[Sukses] Seluruh populasi berhasil dievakuasi pada timestep ke-{t + 1}!")
        break

end_time = time.time()
execution_duration = end_time - start_time

# ==================================================================
# 3. LAPORAN HASIL ANALISIS & INTEGRATOR METRICS
# ==================================================================
df_log = pd.DataFrame(log_history)

print("\n==================================================")
print(" LAPORAN AKHIR ANALISIS KINERJA EVAKUASI")
print("==================================================")
print(f"Waktu Eksekusi Komputasi : {execution_duration:.4f} detik")  # <-- Diperbaiki di sini
print(f"Total Agen Terkelola     : {TOTAL_AGENTS}")
print(f"Tingkat Keberhasilan     : {(np.sum(system.status == 1) / TOTAL_AGENTS) * 100:.2f}%")
print(f"Durasi Waktu Evakuasi    : {len(df_log)} Iterasi Timestep")

print("\n[Ringkasan Data Log (5 Timestep Terakhir)]:")
print(df_log.tail())

print("\n==================================================")
print(" PERSPEKTIF INTEGRATOR & HPC (Kesimpulan Materi):")
print("==================================================")
print("1. Kompleksitas Skala: Ketika jumlah agen dinaikkan dari ribuan")
print("   menjadi jutaan (misalnya evakuasi skala satu kota penuh), memori")
print("   dan kapasitas CPU tunggal akan kewalahan.")
print("2. Peran HPC: Di sinilah infrastruktur HPC dan pemrosesan paralel")
print("   (Message Passing Interface / GPU Acceleration) sangat dibutuhkan")
print("   untuk menghitung skenario bencana secara real-time.")
print("3. Peran Mahasiswa Informatika: Bertindak sebagai 'Integrator'")
print("   yang merumuskan masalah lokal nyata (bencana/evakuasi) ke dalam")
print("   model matematis dan skrip komputasi yang efisien.")
print("==================================================")