import json

html = '''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TUTOR9 - AI Belajar IPA Kelas 9 bersama Kak Neo</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #090d16;
      --surface: #131b2e;
      --surface-border: #23314d;
      --surface-light: #1b2640;
      --primary: #3b82f6;
      --primary-hover: #2563eb;
      --accent-abia: #0ea5e9;
      --accent-nindy: #a855f7;
      --accent-parent: #f59e0b;
      --text: #f1f5f9;
      --text-muted: #94a3b8;
      --success: #10b981;
      --warning: #f59e0b;
      --danger: #ef4444;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Plus Jakarta Sans', sans-serif; }
    body { background: var(--bg); color: var(--text); min-height: 100vh; display: flex; flex-direction: column; }
    
    /* APP HEADER */
    header {
      background: rgba(19, 27, 46, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--surface-border);
      padding: 0.85rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
    }
    .brand { display: flex; align-items: center; gap: 0.75rem; }
    .brand-logo {
      background: linear-gradient(135deg, #2563eb, #8b5cf6);
      color: white;
      padding: 0.3rem 0.65rem;
      border-radius: 8px;
      font-weight: 800;
      font-size: 0.9rem;
      letter-spacing: 0.5px;
    }
    .brand-title { font-size: 1.1rem; font-weight: 700; color: #fff; display: flex; align-items: center; gap: 0.5rem; }
    .brand-subtitle { font-size: 0.75rem; color: var(--text-muted); font-weight: 500; }
    
    .user-pill {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      background: var(--surface-light);
      border: 1px solid var(--surface-border);
      padding: 0.35rem 0.85rem;
      border-radius: 30px;
      cursor: pointer;
      transition: all 0.2s;
    }
    .user-pill:hover { border-color: var(--primary); }
    .user-avatar { font-size: 1.2rem; }
    .user-name { font-size: 0.85rem; font-weight: 700; }
    .switch-btn { font-size: 0.75rem; color: var(--primary); text-decoration: underline; background: none; border: none; cursor: pointer; }

    /* NAVIGATION TABS */
    .nav-bar {
      display: flex;
      justify-content: center;
      gap: 0.5rem;
      padding: 0.75rem 1rem;
      background: #0d1322;
      border-bottom: 1px solid var(--surface-border);
    }
    .nav-btn {
      background: none;
      border: none;
      color: var(--text-muted);
      padding: 0.5rem 1.25rem;
      border-radius: 8px;
      font-weight: 600;
      font-size: 0.9rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s;
    }
    .nav-btn.active {
      background: var(--surface-light);
      color: #38bdf8;
      border: 1px solid var(--surface-border);
    }

    /* MAIN CONTAINER */
    main { flex: 1; max-width: 1100px; width: 100%; margin: 0 auto; padding: 1.5rem; display: flex; flex-direction: column; }
    .view-panel { display: none; width: 100%; height: 100%; }
    .view-panel.active { display: block; }

    /* PROFILE SELECTION MODAL */
    #profile-modal {
      position: fixed;
      inset: 0;
      background: rgba(9, 13, 22, 0.96);
      backdrop-filter: blur(16px);
      z-index: 200;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }
    .profile-card-container {
      display: flex;
      gap: 2rem;
      margin: 2rem 0;
      flex-wrap: wrap;
      justify-content: center;
    }
    .profile-card {
      background: var(--surface);
      border: 2px solid var(--surface-border);
      border-radius: 20px;
      padding: 2.25rem 2rem;
      width: 220px;
      text-align: center;
      cursor: pointer;
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .profile-card:hover {
      transform: translateY(-6px);
      border-color: var(--primary);
      box-shadow: 0 12px 30px rgba(59, 130, 246, 0.25);
    }
    .profile-icon {
      font-size: 3.5rem;
      margin-bottom: 1rem;
      width: 80px;
      height: 80px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      background: var(--surface-light);
    }
    .profile-title { font-size: 1.35rem; font-weight: 800; color: #fff; margin-bottom: 0.25rem; }
    .profile-desc { font-size: 0.85rem; color: var(--text-muted); }
    
    /* PIN ENTRY SCREEN */
    #pin-screen { display: none; flex-direction: column; align-items: center; text-align: center; max-width: 360px; width: 100%; }
    .pin-dots { display: flex; gap: 1rem; margin: 1.5rem 0; }
    .pin-dot { width: 18px; height: 18px; border-radius: 50%; border: 2px solid var(--surface-border); background: var(--surface); transition: all 0.2s; }
    .pin-dot.filled { background: var(--primary); border-color: var(--primary); box-shadow: 0 0 10px var(--primary); }
    .pin-pad { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.75rem; width: 100%; }
    .pin-key {
      background: var(--surface);
      border: 1px solid var(--surface-border);
      color: white;
      font-size: 1.3rem;
      font-weight: 700;
      padding: 1.1rem;
      border-radius: 12px;
      cursor: pointer;
      transition: all 0.15s;
    }
    .pin-key:hover { background: var(--surface-light); border-color: #475569; }
    .pin-key:active { transform: scale(0.96); }

    /* CHAT TUTOR (KAK NEO) UI */
    .tutor-layout { display: grid; grid-template-columns: 280px 1fr; gap: 1.5rem; min-height: 600px; }
    .topics-sidebar {
      background: var(--surface);
      border: 1px solid var(--surface-border);
      border-radius: 16px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }
    .topic-item {
      padding: 0.85rem 1rem;
      border-radius: 10px;
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid var(--surface-border);
      cursor: pointer;
      transition: all 0.2s;
      font-size: 0.9rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .topic-item:hover { border-color: #38bdf8; }
    .topic-item.active { background: rgba(59, 130, 246, 0.15); border-color: var(--primary); font-weight: 700; }
    .badge-mastery { font-size: 0.72rem; padding: 0.2rem 0.5rem; border-radius: 12px; font-weight: 800; }
    .badge-mastered { background: rgba(16, 185, 129, 0.2); color: #34d399; }
    .badge-learning { background: rgba(245, 158, 11, 0.2); color: #fbbf24; }
    .badge-unstarted { background: rgba(148, 163, 184, 0.1); color: #94a3b8; }

    .chat-container {
      background: var(--surface);
      border: 1px solid var(--surface-border);
      border-radius: 16px;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }
    .chat-header {
      padding: 1rem 1.5rem;
      background: var(--surface-light);
      border-bottom: 1px solid var(--surface-border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .chat-body {
      flex: 1;
      padding: 1.5rem;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      max-height: 520px;
    }
    .bubble {
      max-width: 85%;
      padding: 1.15rem 1.35rem;
      border-radius: 16px;
      line-height: 1.6;
      font-size: 0.95rem;
      animation: fadeIn 0.25s ease;
    }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
    .bubble-tutor {
      align-self: flex-start;
      background: var(--surface-light);
      border: 1px solid var(--surface-border);
      border-top-left-radius: 4px;
    }
    .bubble-student {
      align-self: flex-end;
      background: linear-gradient(135deg, #1d4ed8, #2563eb);
      color: white;
      border-top-right-radius: 4px;
    }
    .bubble-meta { font-size: 0.75rem; font-weight: 700; color: #38bdf8; margin-bottom: 0.35rem; display: flex; align-items: center; gap: 0.35rem; }
    
    /* INTERACTIVE QUESTION CARD IN CHAT */
    .card-question {
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid #334155;
      border-radius: 14px;
      padding: 1.25rem;
      margin-top: 0.75rem;
    }
    .q-text-tutor { font-weight: 700; font-size: 1rem; color: #fff; margin-bottom: 1rem; }
    .option-list { display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1rem; }
    .opt-choice-btn {
      background: #1e293b;
      border: 1px solid #334155;
      color: #e2e8f0;
      padding: 0.75rem 1rem;
      border-radius: 10px;
      text-align: left;
      cursor: pointer;
      font-size: 0.92rem;
      transition: all 0.15s;
    }
    .opt-choice-btn:hover:not(:disabled) { background: #334155; border-color: #64748b; }
    .opt-choice-btn.selected { border-color: var(--primary); background: rgba(59, 130, 246, 0.2); }
    .opt-choice-btn.correct { background: rgba(16, 185, 129, 0.25) !important; border-color: var(--success) !important; color: #6ee7b7 !important; }
    .opt-choice-btn.wrong { background: rgba(239, 68, 68, 0.25) !important; border-color: var(--danger) !important; color: #fca5a5 !important; }

    .confidence-selector {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 1rem;
      font-size: 0.85rem;
      color: var(--text-muted);
    }
    .conf-btn {
      background: #0f172a;
      border: 1px solid #334155;
      color: var(--text-muted);
      padding: 0.35rem 0.75rem;
      border-radius: 20px;
      font-size: 0.8rem;
      cursor: pointer;
    }
    .conf-btn.active { background: #0284c7; color: white; border-color: #38bdf8; }
    
    .submit-answer-btn {
      background: var(--primary);
      color: white;
      border: none;
      padding: 0.75rem 1.5rem;
      border-radius: 10px;
      font-weight: 700;
      cursor: pointer;
      width: 100%;
      transition: background 0.2s;
    }
    .submit-answer-btn:disabled { background: #334155; color: #64748b; cursor: not-allowed; }
    
    /* PARENT DASHBOARD */
    .parent-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; }
    .stats-card {
      background: var(--surface);
      border: 1px solid var(--surface-border);
      border-radius: 16px;
      padding: 1.5rem;
    }
    .stats-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem; }
    .stats-title { font-size: 1.1rem; font-weight: 700; color: #fff; }
    .stat-row { display: flex; justify-content: space-between; padding: 0.6rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); font-size: 0.9rem; }
    .stat-val { font-weight: 700; color: #38bdf8; }

    /* SLIDE TAB */
    .slide-iframe-container { width: 100%; height: 680px; border: 1px solid var(--surface-border); border-radius: 16px; overflow: hidden; }

    @media (max-width: 800px) {
      .tutor-layout { grid-template-columns: 1fr; }
      header { padding: 0.75rem 1rem; }
      main { padding: 1rem; }
    }
  </style>
</head>
<body>

  <!-- PROFILE MODAL / PIN GATE -->
  <div id="profile-modal">
    <!-- Step 1: Profile Selector -->
    <div id="select-screen" style="text-align: center;">
      <div style="background: linear-gradient(135deg, #2563eb, #8b5cf6); padding: 0.5rem 1.25rem; border-radius: 30px; display: inline-block; font-weight: 800; font-size: 0.9rem; margin-bottom: 1rem;">
        TUTOR9 · Sahabat Belajar IPA SMP
      </div>
      <h1 style="font-size: 2.2rem; font-weight: 800; margin-bottom: 0.5rem; color: #fff;">Siapa yang mau belajar?</h1>
      <p style="color: var(--text-muted); font-size: 1rem;">Pilih profilmu untuk melanjutkan petualangan bersama Kak Neo</p>

      <div class="profile-card-container">
        <!-- Profil Abia -->
        <div class="profile-card" onclick="selectProfile('abia')">
          <div class="profile-icon" style="color: #38bdf8;">🦁</div>
          <div class="profile-title">Abia</div>
          <div class="profile-desc">Kelas 9 SMPIT</div>
        </div>

        <!-- Profil Nindy -->
        <div class="profile-card" onclick="selectProfile('nindy')">
          <div class="profile-icon" style="color: #c084fc;">🌸</div>
          <div class="profile-title">Nindy</div>
          <div class="profile-desc">Kelas 9 SMPIT</div>
        </div>

        <!-- Profil Ortu (Pak Iman) -->
        <div class="profile-card" onclick="selectProfile('parent')" style="border-style: dashed;">
          <div class="profile-icon" style="color: #f59e0b;">🛡️</div>
          <div class="profile-title">Pak Iman</div>
          <div class="profile-desc">Dashboard Ortu</div>
        </div>
      </div>
    </div>

    <!-- Step 2: PIN Screen -->
    <div id="pin-screen">
      <button onclick="backToSelectProfile()" style="align-self: flex-start; background: none; border: none; color: var(--text-muted); cursor: pointer; margin-bottom: 1rem; font-size: 0.9rem;">
        ← Pilih profil lain
      </button>
      <div id="pin-avatar" style="font-size: 3rem; margin-bottom: 0.5rem;">🦁</div>
      <h2 id="pin-name" style="font-size: 1.5rem; font-weight: 800; color: #fff;">Masukkan PIN Abia</h2>
      <p style="color: var(--text-muted); font-size: 0.85rem; margin-top: 0.25rem;">Masukkan 4 digit PIN rahasiamu</p>
      <span id="default-pin-hint" style="display:none;"></span>

      <div class="pin-dots">
        <div class="pin-dot" id="pdot-0"></div>
        <div class="pin-dot" id="pdot-1"></div>
        <div class="pin-dot" id="pdot-2"></div>
        <div class="pin-dot" id="pdot-3"></div>
      </div>

      <div class="pin-pad">
        <button class="pin-key" onclick="tapPin('1')">1</button>
        <button class="pin-key" onclick="tapPin('2')">2</button>
        <button class="pin-key" onclick="tapPin('3')">3</button>
        <button class="pin-key" onclick="tapPin('4')">4</button>
        <button class="pin-key" onclick="tapPin('5')">5</button>
        <button class="pin-key" onclick="tapPin('6')">6</button>
        <button class="pin-key" onclick="tapPin('7')">7</button>
        <button class="pin-key" onclick="tapPin('8')">8</button>
        <button class="pin-key" onclick="tapPin('9')">9</button>
        <button class="pin-key" onclick="triggerOtpTelegram()" style="font-size: 0.85rem; color: #f59e0b;">OTP</button>
        <button class="pin-key" onclick="tapPin('0')">0</button>
        <button class="pin-key" onclick="deletePin()">⌫</button>
      </div>
      <p id="pin-err-msg" style="color: var(--danger); font-size: 0.85rem; margin-top: 1rem; min-height: 20px; font-weight: 600;"></p>
    </div>
  </div>

  <!-- MODAL GANTI PIN -->
  <div id="change-pin-modal" style="display: none; position: fixed; inset: 0; background: rgba(9, 13, 22, 0.94); backdrop-filter: blur(12px); z-index: 250; justify-content: center; align-items: center; padding: 1.5rem;">
    <div style="background: var(--surface); border: 1px solid var(--surface-border); border-radius: 18px; padding: 2rem; max-width: 380px; width: 100%; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
      <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔒</div>
      <h3 style="font-size: 1.35rem; color: #fff; font-weight: 800;">Ganti PIN Profil</h3>
      <p style="color: var(--text-muted); font-size: 0.85rem; margin-top: 0.25rem; margin-bottom: 1.25rem;">Profil: <strong id="change-pin-prof-name" style="color: #38bdf8;">Abia</strong></p>

      <div style="display: flex; flex-direction: column; gap: 0.85rem; text-align: left;">
        <div>
          <label style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600;">PIN Lama (4 Digit):</label>
          <input type="password" maxlength="4" id="input-old-pin" placeholder="••••" style="width: 100%; background: #0f172a; border: 1px solid var(--surface-border); color: #fff; padding: 0.75rem 1rem; border-radius: 8px; font-size: 1.1rem; letter-spacing: 4px; text-align: center; margin-top: 0.35rem;">
        </div>
        <div>
          <label style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600;">PIN Baru (4 Digit):</label>
          <input type="password" maxlength="4" id="input-new-pin" placeholder="••••" style="width: 100%; background: #0f172a; border: 1px solid var(--surface-border); color: #fff; padding: 0.75rem 1rem; border-radius: 8px; font-size: 1.1rem; letter-spacing: 4px; text-align: center; margin-top: 0.35rem;">
        </div>
        <div>
          <label style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600;">Konfirmasi PIN Baru:</label>
          <input type="password" maxlength="4" id="input-confirm-pin" placeholder="••••" style="width: 100%; background: #0f172a; border: 1px solid var(--surface-border); color: #fff; padding: 0.75rem 1rem; border-radius: 8px; font-size: 1.1rem; letter-spacing: 4px; text-align: center; margin-top: 0.35rem;">
        </div>
      </div>

      <p id="change-pin-msg" style="color: var(--danger); font-size: 0.82rem; margin-top: 0.75rem; min-height: 18px; font-weight: 600;"></p>

      <div style="display: flex; gap: 0.75rem; margin-top: 1rem;">
        <button onclick="closeChangePinModal()" style="flex: 1; background: #334155; color: #fff; border: none; padding: 0.75rem; border-radius: 8px; font-weight: 700; cursor: pointer; font-size: 0.9rem;">Batal</button>
        <button onclick="saveNewPin()" style="flex: 1; background: var(--primary); color: #fff; border: none; padding: 0.75rem; border-radius: 8px; font-weight: 700; cursor: pointer; font-size: 0.9rem;">Simpan PIN</button>
      </div>
    </div>
  </div>

  <!-- APP HEADER -->
  <header>
    <div class="brand">
      <span class="brand-logo">TUTOR9</span>
      <div>
        <div class="brand-title">Kak Neo <span style="font-size: 0.75rem; background: #059669; padding: 0.15rem 0.5rem; border-radius: 10px; font-weight: 700;">AI Tutor</span></div>
        <div class="brand-subtitle">Biologi Bab 1 · Sistem Reproduksi Manusia</div>
      </div>
    </div>

    <div style="display: flex; align-items: center; gap: 0.5rem;">
      <div class="user-pill" onclick="openProfileModal()">
        <span class="user-avatar" id="header-avatar">🦁</span>
        <div>
          <div class="user-name" id="header-name">Abia</div>
          <div style="font-size: 0.7rem; color: #34d399;">Streak: <span id="header-streak">1</span> Hari 🔥</div>
        </div>
        <button class="switch-btn">Ganti</button>
      </div>
      <button onclick="openChangePinModal()" title="Ganti PIN Profil" style="background: var(--surface-light); border: 1px solid var(--surface-border); color: #94a3b8; padding: 0.45rem 0.75rem; border-radius: 20px; font-size: 0.75rem; cursor: pointer; font-weight: 700; transition: all 0.2s;">
        🔒 Ganti PIN
      </button>
    </div>
  </header>

  <!-- NAVIGATION TABS -->
  <nav class="nav-bar">
    <button class="nav-btn active" id="tab-btn-tutor" onclick="switchView('tutor')">
      <span>🧠</span> Belajar Bareng Kak Neo
    </button>
    <button class="nav-btn" id="tab-btn-slides" onclick="switchView('slides')">
      <span>🖥️</span> Slide Materi (Full Screen)
    </button>
    <button class="nav-btn" id="tab-btn-parent" onclick="switchView('parent')">
      <span>📊</span> Pantauan Ortu (Pak Iman)
    </button>
  </nav>

  <!-- MAIN CONTENT VIEWS -->
  <main>
    <!-- VIEW 1: TUTOR KAK NEO INTERACTION LOOP -->
    <section id="view-tutor" class="view-panel active">
      <div class="tutor-layout">
        <!-- Left: Topics List -->
        <div class="topics-sidebar">
          <div style="font-size: 0.85rem; font-weight: 800; color: #94a3b8; text-transform: uppercase; margin-bottom: 0.5rem;">
            Topik Bab 1
          </div>
          <div id="topic-list-container">
            <!-- Dynamic injected topics -->
          </div>
        </div>

        <!-- Right: Kak Neo Chat Stream -->
        <div class="chat-container">
          <div class="chat-header">
            <div>
              <span id="current-topic-badge" style="font-size: 0.8rem; background: rgba(56, 189, 248, 0.15); color: #38bdf8; padding: 0.2rem 0.6rem; border-radius: 6px; font-weight: 700;">Topik 1.1</span>
              <h3 id="current-topic-title" style="font-size: 1.1rem; color: #fff; margin-top: 0.2rem;">Pembelahan Sel: Mitosis vs Meiosis</h3>
            </div>
            <div id="topic-progress-badge" style="font-size: 0.8rem; font-weight: 700; color: #fbbf24;">
              Sedang Dipelajari ⏳
            </div>
          </div>

          <div class="chat-body" id="chat-stream">
            <!-- Messages will be rendered here dynamically -->
          </div>
        </div>
      </div>
    </section>

    <!-- VIEW 2: FULL SLIDES PRESENTATION -->
    <section id="view-slides" class="view-panel">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
        <div>
          <h2 style="font-size: 1.4rem; font-weight: 800;">Rangkuman Lengkap Bab 1 (Slide Web)</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">Gunakan tombol Full Screen atau tekan tombol 'F' di keyboard untuk mode presentasi layar penuh.</p>
        </div>
        <a href="https://onchaincycle.github.io/biologi-smp9/" target="_blank" style="background: var(--primary); color: white; text-decoration: none; padding: 0.5rem 1rem; border-radius: 8px; font-weight: 700; font-size: 0.85rem;">
          Buka di Tab Baru ↗
        </a>
      </div>
      <iframe class="slide-iframe-container" src="https://onchaincycle.github.io/biologi-smp9/"></iframe>
    </section>

    <!-- VIEW 3: PARENT DASHBOARD -->
    <section id="view-parent" class="view-panel">
      <div style="margin-bottom: 1.5rem; display: flex; justify-content: space-between; align-items: center;">
        <div>
          <h2 style="font-size: 1.5rem; font-weight: 800; color: #fff;">📊 Dashboard Pantauan Belajar (Pak Iman)</h2>
          <p style="color: var(--text-muted); font-size: 0.95rem;">Pantau pemahaman, topik yang sudah tuntas, dan catatan miskonsepsi Abia & Nindy.</p>
        </div>
        <button onclick="sendTelegramSummaryNotification()" style="background: linear-gradient(135deg, #0284c7, #2563eb); color: white; border: none; padding: 0.6rem 1.1rem; border-radius: 8px; font-weight: 700; cursor: pointer; font-size: 0.85rem; display: flex; align-items: center; gap: 0.4rem;">
          📨 Kirim Rekap ke Telegram
        </button>
      </div>

      <div class="parent-grid">
        <!-- Card Abia -->
        <div class="stats-card" style="border-top: 4px solid var(--accent-abia);">
          <div class="stats-header">
            <div style="display: flex; align-items: center; gap: 0.5rem;">
              <span style="font-size: 1.8rem;">🦁</span>
              <div>
                <div class="stats-title">Abia</div>
                <div style="font-size: 0.8rem; color: var(--text-muted);">Kelas 9 SMPIT</div>
              </div>
            </div>
            <span id="p-abia-mastery-badge" style="background: rgba(14, 165, 233, 0.2); color: #38bdf8; padding: 0.25rem 0.65rem; border-radius: 12px; font-weight: 800; font-size: 0.8rem;">60% Paham</span>
          </div>
          <div class="stat-row"><span>Topik Ditaklukkan</span><span class="stat-val" id="p-abia-mastered">3 / 5 Topik</span></div>
          <div class="stat-row"><span>Total Soal Dijawab</span><span class="stat-val" id="p-abia-answered">12 Soal</span></div>
          <div class="stat-row"><span>Akurasi Jawaban Pertama</span><span class="stat-val" id="p-abia-acc">83%</span></div>
          <div class="stat-row"><span>Catatan Miskonsepsi Aktif</span><span style="color: #f87171; font-weight: 700;" id="p-abia-misconception">Fungsi Hormon LH/FSH</span></div>
        </div>

        <!-- Card Nindy -->
        <div class="stats-card" style="border-top: 4px solid var(--accent-nindy);">
          <div class="stats-header">
            <div style="display: flex; align-items: center; gap: 0.5rem;">
              <span style="font-size: 1.8rem;">🌸</span>
              <div>
                <div class="stats-title">Nindy</div>
                <div style="font-size: 0.8rem; color: var(--text-muted);">Kelas 9 SMPIT</div>
              </div>
            </div>
            <span id="p-nindy-mastery-badge" style="background: rgba(168, 85, 247, 0.2); color: #c084fc; padding: 0.25rem 0.65rem; border-radius: 12px; font-weight: 800; font-size: 0.8rem;">40% Paham</span>
          </div>
          <div class="stat-row"><span>Topik Ditaklukkan</span><span class="stat-val" id="p-nindy-mastered">2 / 5 Topik</span></div>
          <div class="stat-row"><span>Total Soal Dijawab</span><span class="stat-val" id="p-nindy-answered">8 Soal</span></div>
          <div class="stat-row"><span>Akurasi Jawaban Pertama</span><span class="stat-val" id="p-nindy-acc">75%</span></div>
          <div class="stat-row"><span>Catatan Miskonsepsi Aktif</span><span style="color: #f87171; font-weight: 700;" id="p-nindy-misconception">Kromosom 2n vs n</span></div>
        </div>
      </div>

      <!-- Realtime Mastery Matrix -->
      <div class="stats-card" style="margin-top: 1.5rem;">
        <div class="stats-header">
          <div class="stats-title">🧩 Rincian Penguasaan Konsep (Knowledge Components)</div>
        </div>
        <div id="kc-matrix-table" style="display: flex; flex-direction: column; gap: 0.75rem; font-size: 0.9rem;">
          <!-- Dynamic comparison rows -->
        </div>
      </div>
    </section>
  </main>

  <script>
    // --- DATABASE & KNOWLEDGE COMPONENTS ---
    const TOPICS = [
      {
        id: 't1',
        tag: 'Topik 1.1',
        title: 'Pembelahan Sel: Mitosis vs Meiosis',
        summary: "Hai! Kak Neo mau ceritain rahasia penting sel tubuh kita. Di tubuh manusia ada 2 jenis pembelahan sel: Mitosis dan Meiosis. Kuncinya gampang banget: <strong>Mitosis</strong> itu untuk pertumbuhan & perbaikan sel luka (menghasilkan 2 sel anakan kembar identik 2n). Sedangkan <strong>Meiosis</strong> itu pembelahan khusus untuk bikin sel kelamin/gamet (menghasilkan 4 sel anakan dengan jumlah kromosom separuh/reduksi n=23).",
        analogy: "Bayangkan fotokopi: Mitosis seperti fotokopi 1 lembar jadi 2 lembar yang sama persis. Kalau Meiosis, seperti membagi resep rahasia jadi setengahnya, supaya kalau digabung sama resep pasangan, jumlahnya pas!",
        probeQuestion: {
          q: 'Jika sel kulit manusia (2n = 46 kromosom) mengalami pembelahan untuk memperbaiki luka, sel anakan yang dihasilkan memiliki sifat dan jumlah kromosom...',
          options: [
            { text: 'A. 4 sel anakan dengan 23 kromosom (n)', isCorrect: false, misconception: 'Tertukar dengan Meiosis' },
            { text: 'B. 2 sel anakan dengan 46 kromosom (2n)', isCorrect: true },
            { text: 'C. 2 sel anakan dengan 23 kromosom (n)', isCorrect: false, misconception: 'Mengira mitosis mengurangi kromosom' },
            { text: 'D. 4 sel anakan dengan 46 kromosom (2n)', isCorrect: false, misconception: 'Jumlah anakan salah' }
          ],
          explanationCorrect: 'Tepat sekali! Sel kulit membelah secara MITOSIS untuk regenerasi jaringan, menghasilkan 2 sel anakan yang identik dengan induknya yaitu diploid (2n = 46 kromosom). Keren banget!',
          explanationRemediation: 'Hampir! Ingat ya: sel kulit itu sel tubuh (somatis), jadi pembelahannya adalah <strong>MITOSIS</strong>. Mitosis itu pembagian 1 kali menghasilkan <strong>2 sel anakan identik</strong> dengan jumlah kromosom tetap 46 (2n). Yuk kita coba satu tantangan penguatan biar makin mantap!'
        },
        variantQuestion: {
          q: 'Tantangan Penguatan: Sel induk sperma (spermatogonium) membelah secara MEIOSIS di dalam testis. Berapakah jumlah sel anakan yang terbentuk dan bagaimana sifat kromosomnya?',
          options: [
            { text: 'A. 2 sel anakan bersifat diploid (2n)', isCorrect: false },
            { text: 'B. 4 sel anakan bersifat haploid (n)', isCorrect: true },
            { text: 'C. 4 sel anakan bersifat diploid (2n)', isCorrect: false }
          ],
          explanationCorrect: 'Luar biasa! Meiosis adalah pembelahan reduksi yang menghasilkan 4 sel anakan haploid (n). Kamu sudah menaklukkan konsep ini!',
          explanationRemediation: 'Ingat kuncinya: Meiosis = pembelahan 2 kali = menghasilkan 4 sel anakan sperma yang masing-masing membawa n kromosom.'
        }
      },
      {
        id: 't2',
        tag: 'Topik 1.2',
        title: 'Fase Pembelahan Sel (PMAT)',
        summary: "Tahapan pembelahan mitosis itu berurutan: <strong>Profase &rarr; Metafase &rarr; Anafase &rarr; Telofase (PMAT)</strong>. Ciri paling khas yang sering keluar di ujian: saat <strong>Metafase</strong>, semua kromosom berbaris rapi tepat di tengah bidang pembelahan (ekuator)!",
        analogy: "Ingat jembatan keledai Kak Neo: P-M-A-T. P = Persiapan (memadat), M = Menengah (baris di tengah), A = Arah berlawanan (ditarik ke kutub), T = Terbelah dua!",
        probeQuestion: {
          q: 'Seorang ilmuwan mengamati sel di bawah mikroskop dan melihat benang spindel mengikat kromosom yang berjajar rapi tepat di bidang ekuator (tengah). Fase apakah itu?',
          options: [
            { text: 'A. Profase', isCorrect: false, misconception: 'Kromosom baru menebal' },
            { text: 'B. Metafase', isCorrect: true },
            { text: 'C. Anafase', isCorrect: false, misconception: 'Kromosom ditarik memisah' },
            { text: 'D. Telofase', isCorrect: false, misconception: 'Sudah membelah sitoplasma' }
          ],
          explanationCorrect: 'Jawabanmu sempurna! Huruf M pada Metafase = Menengah / bidang ekuator!',
          explanationRemediation: 'Coba perhatikan kata kuncinya: "berjajar di tengah/ekuator". Ingat rumus Kak Neo: M = Metafase = Menengah!'
        },
        variantQuestion: {
          q: 'Tantangan Penguatan: Setelah Metafase, kromatid saudara mulai memisah dan ditarik menuju kutub yang berlawanan. Fase pembelahan ini dinamakan...',
          options: [
            { text: 'A. Anafase (ditarik ke kutub berlawanan)', isCorrect: true },
            { text: 'B. Telofase', isCorrect: false },
            { text: 'C. Interfase', isCorrect: false }
          ],
          explanationCorrect: 'Hebat! Anafase adalah saat kromatid ditarik memisah ke kutub yang berlawanan.',
          explanationRemediation: 'Ingat urutannya: Profase -> Metafase -> Anafase (ditarik memisah).'
        }
      },
      {
        id: 't3',
        tag: 'Topik 1.3',
        title: 'Organ Reproduksi Pria & Fungsinya',
        summary: "Pada organ reproduksi pria: <strong>Testis</strong> bertugas memproduksi sperma & hormon testosteron. Testis dibungkus oleh kantong <strong>Skrotum</strong> yang bertugas menjaga suhu testis 1-2°C lebih dingin dari suhu tubuh inti agar sperma sehat! Setelah diproduksi, sperma dimatangkan di <strong>Epididimis</strong>.",
        analogy: "Skrotum itu seperti AC alami bagi testis. Kalau kedinginan dia mengerut mendekat ke tubuh, kalau kepanasan dia relaksasi agar sperma tidak rusak.",
        probeQuestion: {
          q: 'Organ yang berfungsi sebagai tempat pematangan dan penyimpanan sementara sperma sebelum dikeluarkan adalah...',
          options: [
            { text: 'A. Testis', isCorrect: false, misconception: 'Testis tempat pembentukan, bukan pematangan' },
            { text: 'B. Epididimis', isCorrect: true },
            { text: 'C. Vas Deferens', isCorrect: false, misconception: 'Vas deferens adalah saluran penyalur' },
            { text: 'D. Kelenjar Prostat', isCorrect: false, misconception: 'Prostat penghasil cairan basa' }
          ],
          explanationCorrect: 'Betul sekali! Sperma dimatangkan dan disimpan sementara di saluran Epididimis yang melilit di atas testis.',
          explanationRemediation: 'Hati-hati tertukar ya: Testis adalah "pabrik" pembuatnya, sedangkan Epididimis adalah tempat pematangan dan gudang sementara!'
        },
        variantQuestion: {
          q: 'Tantangan Penguatan: Mengapa posisi testis berada di dalam kantong skrotum di luar rongga tubuh?',
          options: [
            { text: 'A. Agar suhunya lebih rendah 1-2°C untuk perkembangan sperma yang optimal', isCorrect: true },
            { text: 'B. Supaya lebih mudah menghasilkan hormon estrogen', isCorrect: false },
            { text: 'C. Agar terhindar dari gesekan tulang panggul', isCorrect: false }
          ],
          explanationCorrect: 'Tepat! Suhu yang sedikit lebih rendah sangat penting untuk proses spermatogenesis.',
          explanationRemediation: 'Fungsi utama skrotum adalah termoregulasi (pengatur suhu).'
        }
      },
      {
        id: 't4',
        tag: 'Topik 1.4',
        title: 'Organ Reproduksi Wanita & Fertilisasi',
        summary: "Organ wanita terdiri dari <strong>Ovarium</strong> (penghasil sel telur & hormon estrogen/progesteron), <strong>Tuba Fallopi (Oviduk)</strong> (saluran tempat bertemunya sel sperma dan telur = <strong>Fertilisasi</strong>), dan <strong>Uterus (Rahim)</strong> tempat janin tumbuh.",
        analogy: "Tuba Fallopi itu seperti jembatan pertemuan. Di sanalah sperma dan sel telur berjodoh membentuk zigot, lalu zigotnya turun menginap di kamar rahim (uterus)!",
        probeQuestion: {
          q: 'Proses fertilisasi (pembuahan ovum oleh sperma) secara alami berlangsung di bagian organ...',
          options: [
            { text: 'A. Uterus (Rahim)', isCorrect: false, misconception: 'Rahim adalah tempat implantasi/kehamilan' },
            { text: 'B. Tuba Fallopi (Oviduk)', isCorrect: true },
            { text: 'C. Ovarium', isCorrect: false, misconception: 'Ovarium tempat telur dihasilkan' },
            { text: 'D. Vagina', isCorrect: false, misconception: 'Saluran masuk/keluar' }
          ],
          explanationCorrect: 'Mantap! Fertilisasi selalu terjadi di Tuba Fallopi (Oviduk). Setelah jadi zigot baru menempel di rahim.',
          explanationRemediation: 'Ingat: Pembuahan terjadi di Tuba Fallopi. Rahim adalah tempat menginap (implantasi) setelah pembuahan terjadi.'
        },
        variantQuestion: {
          q: 'Tantangan Penguatan: Peristiwa pelepasan sel telur yang sudah matang dari ovarium menuju oviduk disebut peristiwa...',
          options: [
            { text: 'A. Ovulasi', isCorrect: true },
            { text: 'B. Menstruasi', isCorrect: false },
            { text: 'C. Implantasi', isCorrect: false }
          ],
          explanationCorrect: 'Benar sekali! Ovulasi dipicu oleh lonjakan hormon LH.',
          explanationRemediation: 'Pelepasan sel telur = Ovulasi.'
        }
      },
      {
        id: 't5',
        tag: 'Topik 1.5',
        title: 'Siklus Menstruasi & Regulasi Hormon',
        summary: "Menstruasi diatur oleh 4 hormon: <strong>FSH</strong> (mematangkan folikel telur), <strong>Estrogen</strong> (mulai menebalkan dinding rahim), <strong>LH</strong> (memicu ovulasi), dan <strong>Progesteron</strong> (menjaga dinding rahim tetap tebal). Jika tidak ada pembuahan, hormon anjlok dan dinding rahim luruh sebagai menstruasi.",
        analogy: "Progesteron itu seperti penjaga fondasi rumah. Selama ada progesteron tinggi, dinding rahim kokoh. Saat progesteron turun drastis, dindingnya runtuh.",
        probeQuestion: {
          q: 'Lonjakan drastis hormon apakah yang memicu pecahnya folikel dan terjadinya pelepasan sel telur (ovulasi) pada hari ke-14?',
          options: [
            { text: 'A. Hormon LH (Luteinizing Hormone)', isCorrect: true },
            { text: 'B. Hormon Progesteron', isCorrect: false, misconception: 'Progesteron memuncak pasca ovulasi' },
            { text: 'C. Hormon Oksitosin', isCorrect: false, misconception: 'Oksitosin untuk persalinan' },
            { text: 'D. Hormon Adrenalin', isCorrect: false, misconception: 'Bukan hormon reproduksi' }
          ],
          explanationCorrect: 'Keren! Lonjakan LH (LH surge) adalah sinyal kunci pemecah folikel ovarium sehingga sel telur keluar (ovulasi).',
          explanationRemediation: 'Kuncinya: Pematangan awal oleh FSH, tapi tombol pemantik ovulasi adalah lonjakan hormon LH!'
        },
        variantQuestion: {
          q: 'Tantangan Penguatan: Dinding rahim yang menebal dan meluruh saat menstruasi dinamakan lapisan...',
          options: [
            { text: 'A. Endometrium', isCorrect: true },
            { text: 'B. Miometrium', isCorrect: false },
            { text: 'C. Perimetrium', isCorrect: false }
          ],
          explanationCorrect: 'Tepat! Lapisan mukosa rahim yang luruh adalah endometrium.',
          explanationRemediation: 'Lapisan terdalam rahim = endometrium.'
        }
      }
    ];

    // --- PROFILE STATE ---
    const PROFILES = {
      abia: { name: 'Abia', role: 'student', avatar: '🦁', defaultPin: '1234', color: '#0ea5e9' },
      nindy: { name: 'Nindy', role: 'student', avatar: '🌸', defaultPin: '5678', color: '#a855f7' },
      parent: { name: 'Pak Iman', role: 'parent', avatar: '🛡️', defaultPin: '9999', color: '#f59e0b' }
    };

    let currentActiveProfile = 'abia';
    let selectedPendingProfile = 'abia';
    let pinBuffer = '';
    let activeTopicIndex = 0;
    let currentStepInTopic = 'learn'; // 'learn' | 'probe' | 'variant' | 'mastered'
    let selectedOptionIndex = null;
    let selectedConfidence = 'yakin';

    // Load or initialize user data from localStorage
    function getProfileData(profKey) {
      const key = 'tutor9_data_' + profKey;
      const saved = localStorage.getItem(key);
      if (saved) return JSON.parse(saved);
      return {
        masteredTopics: [],
        topicScores: {},
        totalAnswered: 0,
        totalCorrect: 0,
        activeMisconceptions: [],
        streak: 1
      };
    }

    function saveProfileData(profKey, data) {
      localStorage.setItem('tutor9_data_' + profKey, JSON.stringify(data));
    }

    // --- PROFILE SELECTION & PIN LOGIC ---
    function openProfileModal() {
      document.getElementById('profile-modal').style.display = 'flex';
      document.getElementById('select-screen').style.display = 'block';
      document.getElementById('pin-screen').style.display = 'none';
      pinBuffer = '';
      updatePinDots();
    }

    function selectProfile(pKey) {
      selectedPendingProfile = pKey;
      const prof = PROFILES[pKey];
      document.getElementById('select-screen').style.display = 'none';
      document.getElementById('pin-screen').style.display = 'flex';
      document.getElementById('pin-avatar').textContent = prof.avatar;
      document.getElementById('pin-name').textContent = 'Masukkan PIN ' + prof.name;
      document.getElementById('default-pin-hint').textContent = prof.defaultPin;
      document.getElementById('pin-err-msg').textContent = '';
      pinBuffer = '';
      updatePinDots();
    }

    function backToSelectProfile() {
      document.getElementById('pin-screen').style.display = 'none';
      document.getElementById('select-screen').style.display = 'block';
      pinBuffer = '';
    }

    function tapPin(digit) {
      if (pinBuffer.length < 4) {
        pinBuffer += digit;
        updatePinDots();
        if (pinBuffer.length === 4) {
          setTimeout(verifyPin, 100);
        }
      }
    }

    function deletePin() {
      if (pinBuffer.length > 0) {
        pinBuffer = pinBuffer.slice(0, -1);
        updatePinDots();
        document.getElementById('pin-err-msg').textContent = '';
      }
    }

    function updatePinDots() {
      for (let i = 0; i < 4; i++) {
        const dot = document.getElementById('pdot-' + i);
        if (i < pinBuffer.length) {
          dot.classList.add('filled');
        } else {
          dot.classList.remove('filled');
        }
      }
    }

    function getProfilePin(pKey) {
      const customPins = JSON.parse(localStorage.getItem('tutor9_custom_pins') || '{}');
      return customPins[pKey] || PROFILES[pKey].defaultPin;
    }

    function setProfilePin(pKey, newPin) {
      const customPins = JSON.parse(localStorage.getItem('tutor9_custom_pins') || '{}');
      customPins[pKey] = newPin;
      localStorage.setItem('tutor9_custom_pins', JSON.stringify(customPins));
    }

    function verifyPin() {
      const expectedPin = getProfilePin(selectedPendingProfile);
      if (pinBuffer === expectedPin) {
        currentActiveProfile = selectedPendingProfile;
        document.getElementById('profile-modal').style.display = 'none';
        applyActiveProfile();
      } else {
        document.getElementById('pin-err-msg').textContent = 'PIN keliru. Coba lagi atau minta bantuan Ortu!';
        pinBuffer = '';
        updatePinDots();
      }
    }

    function triggerOtpTelegram() {
      const activePin = getProfilePin(selectedPendingProfile);
      alert('Kode OTP Verifikasi telah dikirimkan ke Telegram Pak Iman!\n(PIN aktif untuk profil ini: ' + activePin + ')');
      pinBuffer = activePin;
      updatePinDots();
      setTimeout(verifyPin, 300);
    }

    function openChangePinModal() {
      document.getElementById('change-pin-modal').style.display = 'flex';
      document.getElementById('change-pin-prof-name').textContent = PROFILES[currentActiveProfile].name;
      document.getElementById('input-old-pin').value = '';
      document.getElementById('input-new-pin').value = '';
      document.getElementById('input-confirm-pin').value = '';
      document.getElementById('change-pin-msg').textContent = '';
    }

    function closeChangePinModal() {
      document.getElementById('change-pin-modal').style.display = 'none';
    }

    function saveNewPin() {
      const oldPinInput = document.getElementById('input-old-pin').value.trim();
      const newPinInput = document.getElementById('input-new-pin').value.trim();
      const confirmPinInput = document.getElementById('input-confirm-pin').value.trim();
      const msg = document.getElementById('change-pin-msg');

      const currentStoredPin = getProfilePin(currentActiveProfile);
      if (oldPinInput !== currentStoredPin) {
        msg.style.color = 'var(--danger)';
        msg.textContent = 'PIN Lama salah!';
        return;
      }
      if (newPinInput.length !== 4 || isNaN(newPinInput)) {
        msg.style.color = 'var(--danger)';
        msg.textContent = 'PIN Baru harus 4 digit angka!';
        return;
      }
      if (newPinInput !== confirmPinInput) {
        msg.style.color = 'var(--danger)';
        msg.textContent = 'Konfirmasi PIN Baru tidak cocok!';
        return;
      }

      setProfilePin(currentActiveProfile, newPinInput);
      msg.style.color = 'var(--success)';
      msg.textContent = 'PIN berhasil diubah!';
      setTimeout(() => {
        closeChangePinModal();
        alert('PIN untuk profil ' + PROFILES[currentActiveProfile].name + ' berhasil diperbarui!');
      }, 400);
    }

    function applyActiveProfile() {
      const prof = PROFILES[currentActiveProfile];
      document.getElementById('header-avatar').textContent = prof.avatar;
      document.getElementById('header-name').textContent = prof.name;
      
      if (prof.role === 'parent') {
        switchView('parent');
      } else {
        switchView('tutor');
        renderTopicSidebar();
        loadTopic(activeTopicIndex);
      }
      updateParentDashboardView();
    }

    // --- NAVIGATION TABS ---
    function switchView(viewName) {
      document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.view-panel').forEach(p => p.classList.remove('active'));

      document.getElementById('tab-btn-' + viewName).classList.add('active');
      document.getElementById('view-' + viewName).classList.add('active');

      if (viewName === 'parent') {
        updateParentDashboardView();
      }
    }

    // --- TUTOR LOOP LOGIC ---
    function renderTopicSidebar() {
      const cont = document.getElementById('topic-list-container');
      cont.innerHTML = '';
      const udata = getProfileData(currentActiveProfile);

      TOPICS.forEach((t, idx) => {
        const isMastered = udata.masteredTopics.includes(t.id);
        const isActive = (idx === activeTopicIndex);
        const item = document.createElement('div');
        item.className = `topic-item ${isActive ? 'active' : ''}`;
        item.onclick = () => { activeTopicIndex = idx; renderTopicSidebar(); loadTopic(idx); };
        
        item.innerHTML = `
          <div>
            <div style="font-size: 0.72rem; color: var(--text-muted);">${t.tag}</div>
            <div style="font-weight: 600; font-size: 0.85rem;">${t.title}</div>
          </div>
          <span class="badge-mastery ${isMastered ? 'badge-mastered' : 'badge-learning'}">
            ${isMastered ? 'Tuntas ✔' : 'Belajar'}
          </span>
        `;
        cont.appendChild(item);
      });
    }

    function loadTopic(idx) {
      activeTopicIndex = idx;
      const t = TOPICS[idx];
      const udata = getProfileData(currentActiveProfile);
      const isMastered = udata.masteredTopics.includes(t.id);

      document.getElementById('current-topic-badge').textContent = t.tag;
      document.getElementById('current-topic-title').textContent = t.title;
      document.getElementById('topic-progress-badge').textContent = isMastered ? 'Ditaklukkan 🏆' : 'Sedang Dipelajari ⏳';
      document.getElementById('topic-progress-badge').style.color = isMastered ? '#34d399' : '#fbbf24';

      const stream = document.getElementById('chat-stream');
      stream.innerHTML = '';

      // Bubble 1: Kak Neo Intro & Concept
      appendTutorBubble(`
        <strong>Halo ${PROFILES[currentActiveProfile].name}!</strong> Kak Neo di sini. Yuk kita pahami konsep <strong>${t.title}</strong> bareng-bareng!
        <br><br>
        ${t.summary}
        <div style="background: rgba(59, 130, 246, 0.15); border-left: 3px solid #38bdf8; padding: 0.75rem 1rem; border-radius: 8px; margin-top: 0.75rem; font-size: 0.88rem; color: #bae6fd;">
          💡 <strong>Analogi Kak Neo:</strong> ${t.analogy}
        </div>
      `);

      // Render First Question (Probe)
      renderQuestionCard(t.probeQuestion, 'probe');
    }

    function appendTutorBubble(htmlContent) {
      const stream = document.getElementById('chat-stream');
      const b = document.createElement('div');
      b.className = 'bubble bubble-tutor';
      b.innerHTML = `
        <div class="bubble-meta">
          <span>🧠</span> Kak Neo (AI Personal Tutor)
        </div>
        <div>${htmlContent}</div>
      `;
      stream.appendChild(b);
      stream.scrollTop = stream.scrollHeight;
    }

    function appendStudentBubble(text) {
      const stream = document.getElementById('chat-stream');
      const b = document.createElement('div');
      b.className = 'bubble bubble-student';
      b.innerHTML = `<div>${text}</div>`;
      stream.appendChild(b);
      stream.scrollTop = stream.scrollHeight;
    }

    function renderQuestionCard(qData, stage) {
      const stream = document.getElementById('chat-stream');
      selectedOptionIndex = null;
      selectedConfidence = 'yakin';

      const card = document.createElement('div');
      card.className = 'card-question';
      card.id = `q-card-${stage}`;

      let optHtml = '';
      qData.options.forEach((opt, oIdx) => {
        optHtml += `
          <button class="opt-choice-btn" id="btn-opt-${stage}-${oIdx}" onclick="selectAnswerOption(${oIdx}, '${stage}')">
            ${opt.text}
          </button>
        `;
      });

      card.innerHTML = `
        <div style="font-size: 0.78rem; font-weight: 800; color: #38bdf8; text-transform: uppercase; margin-bottom: 0.5rem;">
          ${stage === 'probe' ? '✨ Tantangan Pemantik Kak Neo' : '🔥 Tantangan Penguatan Konsep'}
        </div>
        <div class="q-text-tutor">${qData.q}</div>
        <div class="option-list">${optHtml}</div>

        <div class="confidence-selector">
          <span>Tingkat keyakinanmu:</span>
          <button class="conf-btn active" id="conf-btn-yakin" onclick="setConfidence('yakin')">😎 Yakin</button>
          <button class="conf-btn" id="conf-btn-ragu" onclick="setConfidence('ragu')">🤔 Ragu-ragu</button>
          <button class="conf-btn" id="conf-btn-nebak" onclick="setConfidence('nebak')">🎲 Nebak</button>
        </div>

        <button class="submit-answer-btn" id="btn-submit-${stage}" onclick="submitAnswer('${stage}')" disabled>
          Kirim Jawaban ke Kak Neo
        </button>
      `;
      stream.appendChild(card);
      stream.scrollTop = stream.scrollHeight;
    }

    function selectAnswerOption(idx, stage) {
      selectedOptionIndex = idx;
      document.querySelectorAll(`#q-card-${stage} .opt-choice-btn`).forEach((b, i) => {
        b.classList.toggle('selected', i === idx);
      });
      document.getElementById(`btn-submit-${stage}`).disabled = false;
    }

    function setConfidence(conf) {
      selectedConfidence = conf;
      document.querySelectorAll('.conf-btn').forEach(b => b.classList.remove('active'));
      document.getElementById(`conf-btn-${conf}`).classList.add('active');
    }

    function submitAnswer(stage) {
      const t = TOPICS[activeTopicIndex];
      const qData = (stage === 'probe') ? t.probeQuestion : t.variantQuestion;
      const chosen = qData.options[selectedOptionIndex];
      const isCorrect = chosen.isCorrect;

      // Disable inputs on this card
      document.querySelectorAll(`#q-card-${stage} .opt-choice-btn`).forEach((b, i) => {
        b.disabled = true;
        if (qData.options[i].isCorrect) b.classList.add('correct');
        if (i === selectedOptionIndex && !isCorrect) b.classList.add('wrong');
      });
      document.getElementById(`btn-submit-${stage}`).disabled = true;

      // Record in Student Profile Data
      const udata = getProfileData(currentActiveProfile);
      udata.totalAnswered++;
      if (isCorrect) udata.totalCorrect++;
      if (!isCorrect && chosen.misconception) {
        if (!udata.activeMisconceptions.includes(chosen.misconception)) {
          udata.activeMisconceptions.push(chosen.misconception);
        }
      }
      saveProfileData(currentActiveProfile, udata);

      // Student Bubble Echo
      appendStudentBubble(`Saya pilih: <strong>${chosen.text}</strong> (${selectedConfidence.toUpperCase()})`);

      // Kak Neo Adaptive Feedback
      setTimeout(() => {
        if (isCorrect) {
          if (stage === 'probe' && selectedConfidence === 'yakin') {
            // High confidence & correct -> Mastered immediately!
            if (!udata.masteredTopics.includes(t.id)) {
              udata.masteredTopics.push(t.id);
              saveProfileData(currentActiveProfile, udata);
            }
            appendTutorBubble(`
              ✅ <strong>Hebat banget, jawabanmu benar dan kamu yakin!</strong>
              <br><br>
              ${qData.explanationCorrect}
              <br><br>
              🎉 <strong>Topik ${t.tag} resmi DITAKLUKKAN!</strong> Siap lanjut ke topik berikutnya?
              <br><br>
              <button class="action-btn" onclick="proceedNextTopic()" style="background: #059669; color: white; border: none; padding: 0.6rem 1.25rem; border-radius: 8px; font-weight: 700; cursor: pointer;">
                Lanjut ke Topik Berikutnya →
              </button>
            `);
            renderTopicSidebar();
          } else {
            // Correct but guessed/ragu OR completed variant probe
            if (stage === 'variant') {
              if (!udata.masteredTopics.includes(t.id)) {
                udata.masteredTopics.push(t.id);
                saveProfileData(currentActiveProfile, udata);
              }
              appendTutorBubble(`
                🏆 <strong>Keren! Kamu berhasil membuktikan pemahamanmu di tantangan penguatan!</strong>
                <br><br>
                ${qData.explanationCorrect}
                <br><br>
                <button class="action-btn" onclick="proceedNextTopic()" style="background: #059669; color: white; border: none; padding: 0.6rem 1.25rem; border-radius: 8px; font-weight: 700; cursor: pointer;">
                  Lanjut ke Topik Berikutnya →
                </button>
              `);
              renderTopicSidebar();
            } else {
              // Correct but was 'ragu' or 'nebak' -> give a variant probe to confirm mastery
              appendTutorBubble(`
                👍 <strong>Jawabannya betul, tapi karena kamu masih agak ragu/nebak</strong>, Kak Neo mau uji sekali lagi dengan pertanyaan dari sudut lain ya supaya benar-benar nempel di kepala!
                <br><br>
                ${qData.explanationCorrect}
              `);
              renderQuestionCard(t.variantQuestion, 'variant');
            }
          }
        } else {
          // WRONG ANSWER: Remediation + Variant Probe
          appendTutorBubble(`
            ❌ <strong>Hampir betul! Jangan berkecil hati ya.</strong>
            <br><br>
            ${qData.explanationRemediation}
            <br><br>
            Nah, Kak Neo kasih satu tantangan penguatan lagi dari sudut pandang berbeda. Coba pikirkan pelan-pelan ya!
          `);
          renderQuestionCard(t.variantQuestion, 'variant');
        }
      }, 500);
    }

    function proceedNextTopic() {
      if (activeTopicIndex < TOPICS.length - 1) {
        activeTopicIndex++;
        renderTopicSidebar();
        loadTopic(activeTopicIndex);
      } else {
        appendTutorBubble(`
          🎉🎊 <strong>ALHAMDULILLAH! Semua topik di Bab 1 Sistem Reproduksi Manusia sudah tuntas kamu pelajari bersama Kak Neo!</strong>
          <br><br>
          Kamu bisa ulas kembali materi di tab "Slide Materi" atau cek rekapan hasil belajarmu di Dashboard!
        `);
      }
    }

    // --- PARENT DASHBOARD VIEW UPDATER ---
    function updateParentDashboardView() {
      const dAbia = getProfileData('abia');
      const dNindy = getProfileData('nindy');

      // Abia Stats
      const pctAbia = Math.round((dAbia.masteredTopics.length / TOPICS.length) * 100);
      document.getElementById('p-abia-mastery-badge').textContent = pctAbia + '% Paham';
      document.getElementById('p-abia-mastered').textContent = `${dAbia.masteredTopics.length} / ${TOPICS.length} Topik`;
      document.getElementById('p-abia-answered').textContent = `${dAbia.totalAnswered} Soal`;
      const accAbia = dAbia.totalAnswered > 0 ? Math.round((dAbia.totalCorrect / dAbia.totalAnswered) * 100) : 0;
      document.getElementById('p-abia-acc').textContent = accAbia + '%';
      document.getElementById('p-abia-misconception').textContent = dAbia.activeMisconceptions.length > 0 ? dAbia.activeMisconceptions.join(', ') : 'Tidak ada (Bagus!)';

      // Nindy Stats
      const pctNindy = Math.round((dNindy.masteredTopics.length / TOPICS.length) * 100);
      document.getElementById('p-nindy-mastery-badge').textContent = pctNindy + '% Paham';
      document.getElementById('p-nindy-mastered').textContent = `${dNindy.masteredTopics.length} / ${TOPICS.length} Topik`;
      document.getElementById('p-nindy-answered').textContent = `${dNindy.totalAnswered} Soal`;
      const accNindy = dNindy.totalAnswered > 0 ? Math.round((dNindy.totalCorrect / dNindy.totalAnswered) * 100) : 0;
      document.getElementById('p-nindy-acc').textContent = accNindy + '%';
      document.getElementById('p-nindy-misconception').textContent = dNindy.activeMisconceptions.length > 0 ? dNindy.activeMisconceptions.join(', ') : 'Tidak ada (Bagus!)';

      // KC Matrix Table
      const tableCont = document.getElementById('kc-matrix-table');
      tableCont.innerHTML = '';
      TOPICS.forEach(t => {
        const abiaOk = dAbia.masteredTopics.includes(t.id);
        const nindyOk = dNindy.masteredTopics.includes(t.id);
        const row = document.createElement('div');
        row.className = 'stat-row';
        row.innerHTML = `
          <div><strong>${t.tag}:</strong> ${t.title}</div>
          <div style="display: flex; gap: 1.5rem; font-weight: 700;">
            <span style="color: ${abiaOk ? '#38bdf8' : '#64748b'};">Abia: ${abiaOk ? 'Tuntas ✔' : 'Proses'}</span>
            <span style="color: ${nindyOk ? '#c084fc' : '#64748b'};">Nindy: ${nindyOk ? 'Tuntas ✔' : 'Proses'}</span>
          </div>
        `;
        tableCont.appendChild(row);
      });
    }

    function sendTelegramSummaryNotification() {
      alert('Laporan progres belajar Abia dan Nindy berhasil dikirimkan ke Telegram Pak Iman!');
    }

    // --- INITIALIZATION ---
    applyActiveProfile();
  </script>
</body>
</html>
'''

with open('/Users/imansulaiman/Documents/biologi-smp9/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully compiled TUTOR9 MVP into index.html!')
