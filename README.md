# 📵 Unplug: Digital Detox Pledge & Habit Tracker

A web app that helps you put your phone down. Sign a detox pledge, and Unplug uses your phone's **motion sensors** to track face-down detox sessions, focus time and steps. It also keeps streaks and awards badges.

No login, no backend. All your data stays on your device.

**🔗 Live app:** https://digital-detox-habit-tracker.vercel.app/

---

## 🏠 Today

<p>
  <img src="screenshots/today.jpg" width="260">
  <img src="screenshots/today-charts.jpg" width="260">
</p>

- Progress rings with today's score
- Day streak, best streak, 30-day adherence and grace day
- Offline time, focus time, steps and pickups at a glance
- A 14-day trend chart (Offline / Focus / Steps)
- A 16-week adherence heatmap

## 📴 Detox

<p>
  <img src="screenshots/detox.jpg" width="260">
  <img src="screenshots/telemetry.jpg" width="260">
</p>

- **Open-ended detox:** place your phone face-down and a session starts automatically
- **Focus pledge:** a 15 to 90 minute timer. Picking up the phone or leaving the app counts as a breach
- Focus sounds: pink noise or binaural tones
- **Live telemetry:** 3D phone tilt, motion level and current state (still or moving)
- Keep-screen-awake option and a list of today's sessions

## 🚶 Steps

<p>
  <img src="screenshots/steps.jpg" width="260">
  <img src="screenshots/accelerometer.jpg" width="260">
</p>

- Step counter that uses the phone's accelerometer
- Distance, calories, cadence and active minutes
- Live accelerometer graph with Low / Med / High sensitivity
- **Walk mode** keeps the screen on. **Pocket mode** dims it to save battery
- Steps by hour and over the last 7 days

## 🛡️ Pledges & 🏅 Badges

<p>
  <img src="screenshots/pledges.jpg" width="260">
  <img src="screenshots/badges.jpg" width="260">
</p>

- A signed **"My Digital Detox Pledge"** card
- 7 pledge types: offline time, focus, steps, app limit, phone-free meals, phone-free sleep, custom habit
- A day counts towards your streak when you keep **75%** of your pledges. One missed day a week is forgiven
- **12 badges** to unlock, such as First Flip, 7-Day Detox Titan and 10K Walker

## 👤 Me: Settings, Backup & Device Check

<p>
  <img src="screenshots/settings.jpg" width="260">
  <img src="screenshots/backup.jpg" width="260">
  <img src="screenshots/capabilities.jpg" width="260">
</p>

- Multiple profiles, each with an optional 4-digit PIN
- Theme (Auto / Light / Dark), sound, haptics, sensitivity and height
- Back up your data as **JSON**, or as a **sound file (.wav)** that can be restored later
- A device capabilities check that shows which sensors your phone supports

---

## 🛠️ Tech

Plain HTML, CSS and JavaScript in a single file (about 93 KB) with no frameworks. It uses these browser APIs: Device Motion & Orientation, Wake Lock, Web Audio, Vibration and localStorage.

## 🚀 Run & Deploy

```bash
npm install
npm run build        # builds index.html from src/index.html
python3 serve.py     # local HTTPS server for testing on your phone
```

