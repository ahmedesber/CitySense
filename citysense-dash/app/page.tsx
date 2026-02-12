'use client';
import { useMemo, useState } from 'react';
import Map, { Marker } from 'react-map-gl/mapbox';
import { Activity, ShieldCheck, Zap, Globe } from 'lucide-react';
import 'mapbox-gl/dist/mapbox-gl.css';

export default function Dashboard() {
  // --- DUAL-LOCATION SIMULATION ---
  const allDetections = useMemo(() => {
    // 70 Markers near Istinye University / Kağıthane, Istanbul
    const istanbul = Array.from({ length: 70 }, (_, i) => ({
      id: `tr-${i}`,
      lat: 41.11 + (Math.random() - 0.5) * 0.05,
      lng: 28.98 + (Math.random() - 0.5) * 0.05
    }));

    // 70 Markers near Fujairah, UAE
    const uae = Array.from({ length: 70 }, (_, i) => ({
      id: `uae-${i}`,
      lat: 25.1288 + (Math.random() - 0.5) * 0.05,
      lng: 56.3265 + (Math.random() - 0.5) * 0.05
    }));

    return [...istanbul, ...uae];
  }, []);

  // View state for switching between cities
  const [viewState, setViewState] = useState({
    longitude: 56.3265, // Defaults to Fujairah
    latitude: 25.1288,
    zoom: 12
  });

  return (
    <main className="min-h-screen bg-slate-950 text-white p-8 font-sans">
      {/* Header */}
      <div className="flex justify-between items-end mb-12 border-b border-slate-800 pb-6">
        <div>
          <h1 className="text-5xl font-black tracking-tighter text-blue-500 italic uppercase">CITYSENSE</h1>
          <p className="text-slate-400 font-medium tracking-wide uppercase">AI-Powered Road Monitoring Node</p>
        </div>
        <div className="flex gap-4">
          <button
            onClick={() => setViewState({ longitude: 28.9784, latitude: 41.0082, zoom: 11 })}
            className="bg-slate-900 border border-slate-700 px-4 py-2 rounded-xl text-xs font-bold hover:border-blue-500 transition-all uppercase"
          >
            🇹🇷 Istanbul
          </button>
          <button
            onClick={() => setViewState({ longitude: 56.3265, latitude: 25.1288, zoom: 11 })}
            className="bg-slate-900 border border-slate-700 px-4 py-2 rounded-xl text-xs font-bold hover:border-blue-500 transition-all uppercase"
          >
            🇦🇪 Fujairah
          </button>
        </div>
      </div>

      {/* Metrics */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
        <MetricCard title="Model Performance" value="0.87 F1" icon={<Activity className="text-blue-500" />} subtitle="Validated on YOLOv8" />
        <MetricCard title="Total Detections" value="140" icon={<ShieldCheck className="text-green-500" />} subtitle="Istanbul & UAE Nodes" />
        <MetricCard title="5G Edge Latency" value="12ms" icon={<Zap className="text-yellow-500" />} subtitle="Optimized for M1 Air" />
      </div>

      {/* Map */}
      <div className="relative h-[600px] rounded-[2.5rem] overflow-hidden border border-slate-800 shadow-[0_0_50px_-12px_rgba(59,130,246,0.3)]">
        <Map
          {...viewState}
          onMove={evt => setViewState(evt.viewState)}
          style={{ width: '100%', height: '100%' }}
          mapStyle="mapbox://styles/mapbox/dark-v11"
          mapboxAccessToken="pk.eyJ1IjoiYWhtZWRlc2JlciIsImEiOiJjbWxndG02OGUwMXBuM2ZzZnE4czcwdHZ0In0._1pXoIwf7O9eyXosUliBag"
        >
          {allDetections.map((p) => (
            <Marker key={p.id} longitude={p.lng} latitude={p.lat}>
              <div className="w-3 h-3 bg-red-500 rounded-full border border-white shadow-[0_0_8px_red] animate-pulse" />
            </Marker>
          ))}
        </Map>
      </div>
    </main>
  );
}

function MetricCard({ title, value, icon, subtitle }: { title: string, value: string, icon: any, subtitle: string }) {
  return (
    <div className="bg-slate-900/40 backdrop-blur-sm border border-slate-800 p-8 rounded-[2rem] hover:border-blue-500/50 transition-all group">
      <div className="flex items-center gap-3 text-slate-400 mb-4 group-hover:text-blue-400 transition-colors uppercase text-xs font-bold tracking-widest">
        {icon} {title}
      </div>
      <div className="text-5xl font-black mb-1 tracking-tight">{value}</div>
      <div className="text-slate-500 text-sm font-medium">{subtitle}</div>
    </div>
  );
}