// static/script.js

const cropData = {
  rice: { soil: "Clayey, loamy", temperature: "20-30°C", region: "Eastern & Southern India", season: "Kharif" },
  maize: { soil: "Well-drained alluvial", temperature: "21-27°C", region: "Punjab, Bihar", season: "Kharif" },
  chickpea: { soil: "Loamy, well-drained", temperature: "25-30°C", region: "Central & Western India", season: "Rabi" },
  kidneybeans: { soil: "Well-drained sandy loam", temperature: "20-25°C", region: "North & Central India", season: "Rabi" },
  pigeonpeas: { soil: "Loamy, sandy", temperature: "25-30°C", region: "Southern India", season: "Kharif" },
  mothbeans: { soil: "Sandy, well-drained", temperature: "30-40°C", region: "Rajasthan, Gujarat", season: "Kharif" },
  mungbean: { soil: "Well-drained, sandy loam", temperature: "25-35°C", region: "North & Central India", season: "Kharif" },
  blackgram: { soil: "Loamy, fertile", temperature: "25-30°C", region: "Southern & Central India", season: "Kharif" },
  lentil: { soil: "Well-drained, loamy", temperature: "15-20°C", region: "Northern India", season: "Rabi" },
  pomegranate: { soil: "Well-drained sandy, loamy", temperature: "30-35°C", region: "Maharashtra, Andhra Pradesh", season: "Post-monsoon" },
  banana: { soil: "Well-drained, sandy loam", temperature: "25-30°C", region: "Tamil Nadu, Kerala", season: "All year round" },
  mango: { soil: "Well-drained, sandy loam", temperature: "25-35°C", region: "Maharashtra, Uttar Pradesh", season: "Summer" },
  grapes: { soil: "Well-drained, slightly acidic", temperature: "20-25°C", region: "Maharashtra, Karnataka", season: "Winter" },
  watermelon: { soil: "Loamy, sandy", temperature: "25-30°C", region: "Punjab, Rajasthan", season: "Summer" },
  muskmelon: { soil: "Loamy, well-drained", temperature: "25-35°C", region: "North India", season: "Summer" },
  apple: { soil: "Well-drained, loamy", temperature: "10-20°C", region: "Jammu & Kashmir", season: "Autumn" },
  orange: { soil: "Loamy, well-drained", temperature: "25-35°C", region: "Maharashtra, Gujarat", season: "Winter" },
  papaya: { soil: "Sandy loam, well-drained", temperature: "25-30°C", region: "Kerala, Tamil Nadu", season: "All year round" },
  coconut: { soil: "Sandy loam, well-drained", temperature: "25-30°C", region: "Kerala, Tamil Nadu", season: "All year round" },
  cotton: { soil: "Loamy, well-drained", temperature: "25-30°C", region: "Maharashtra, Gujarat", season: "Kharif" },
  jute: { soil: "Silty loam, well-drained", temperature: "30-35°C", region: "West Bengal, Bihar", season: "Kharif" },
  coffee: { soil: "Well-drained, rich in organic matter", temperature: "18-25°C", region: "Karnataka, Kerala", season: "Monsoon" },
};

function showCropInfo(cropName) {
  const info = cropData[cropName];
  if (!info) return;

  document.getElementById("crop-name").textContent = cropName.charAt(0).toUpperCase() + cropName.slice(1);
  document.getElementById("crop-soil").textContent = info.soil;
  document.getElementById("crop-temp").textContent = info.temperature;
  document.getElementById("crop-region").textContent = info.region;
  document.getElementById("crop-season").textContent = info.season;

  document.getElementById("crop-info").style.display = "block";
}
