'use client';
// Consolidated imports to prevent duplication errors
import { Map, Marker } from 'react-map-gl'; 
import { Activity, ShieldCheck, Zap } from 'lucide-react';
import 'mapbox-gl/dist/mapbox-gl.css';

// Ensure detections.json is in citysense-dash/data/
import detections from '../data/detections.json';

export default function Dashboard() {
  return (
    <main className="min-h-screen bg-slate-950 text-white p-8 font-sans">
      {/* 1. Dashboard Header */}
      <div className="flex justify-between items-end mb-12 border-b border-slate-800 pb-6">
        <div>
          <h1 className="text-5xl font-black tracking-tighter text-blue-500 italic uppercase">CITYSENSE</h1>
          <p className="text-slate-400 font-medium tracking-wide uppercase">AI-Powered Road Monitoring Node</p>
        </div>
        <div className="text-right">
          <div className="bg-blue-500/10 border border-blue-500/50 text-blue-400 px-4 py-1 rounded-full text-xs font-mono uppercase tracking-widest mb-2">
            Status: Active (Fujairah, UAE)
          </div>
          <p className="text-slate-500 text-xs font-mono">NODE ID: DXB-2026-001</p>
        </div>
      </div>

      {/* 2. Pro Metric Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
        {/* Your 0.87 F1-score model is the core of this project */}
        <MetricCard title="Model Performance" value="0.87 F1" icon={<Activity className="text-blue-500" />} subtitle="Validated on YOLOv8" />
        {/* Shows your 140 detections from the Fujairah field test */}
        <MetricCard title="Detection Count" value={detections.length.toString()} icon={<ShieldCheck className="text-green-500" />} subtitle="Active Pothole Markers" />
        <MetricCard title="5G Edge Latency" value="12ms" icon={<Zap className="text-yellow-500" />} subtitle="Fujairah Test Node" />
      </div>

      {/* 3. The Map Display */}
      <div className="relative h-[600px] rounded-[2.5rem] overflow-hidden border border-slate-800 shadow-[0_0_50px_-12px_rgba(59,130,246,0.3)]">
        <Map
          initialViewState={{ longitude: 56.3265, latitude: 25.1288, zoom: 15 }}
          style={{ width: '100%', height: '100%' }}
          mapStyle="mapbox://styles/mapbox/dark-v11"
          mapboxAccessToken="YOUR_MAPBOX_TOKEN" // <-- PASTE YOUR ACTUAL KEY HERE
        >
          {detections.map((pothole) => (
            <Marker 
              key={pothole.id} 
              longitude={pothole.location.lng} 
              latitude={pothole.location.lat}
            >
              <div className="w-4 h-4 bg-red-500 rounded-full border-2 border-white shadow-[0_0_10px_red] animate-pulse" />
            </Marker>
          ))}
        </Map>
        
        <div className="absolute top-6 left-6 bg-slate-950/80 backdrop-blur-md border border-slate-800 p-4 rounded-2xl">
          <p className="text-xs text-slate-400 uppercase font-bold tracking-widest mb-1">Live Feed</p>
          <div className="flex items-center gap-2">
            <div className="w-2 h-2 bg-red-500 rounded-full animate-pulse" />
            <p className="text-sm font-mono text-white italic uppercase tracking-wider">Synced: {detections.length} Detections</p>
          </div>
        </div>
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