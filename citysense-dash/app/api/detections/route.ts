import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

// This MUST be exported as an async function for Next.js to recognize it
export async function GET() {
  try {
    // We are looking inside the citysense-dash folder now
    const filePath = path.join(process.cwd(), 'detections.json');

    // Check if the file exists before reading to avoid crashing the build
    if (!fs.existsSync(filePath)) {
      return NextResponse.json({ error: 'Data file not found' }, { status: 404 });
    }

    const fileData = fs.readFileSync(filePath, 'utf8');
    return NextResponse.json(JSON.parse(fileData));
  } catch (error) {
    return NextResponse.json({ error: 'Failed to load data' }, { status: 500 });
  }
}