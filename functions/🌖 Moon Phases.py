def moon_phase(phase):
  if phase == "New Moon":
    phase = "🌑"
  elif phase == "Waxing Crescent":
    phase = "🌒"
  elif phase == "First Quarter":
    phase = "🌓"
  elif phase == "Waxing Gibbous":
    phase = "🌔"
  elif phase == "Full Moon":
    phase = "🌕"
  elif phase == "Waning Gibbous":
    phase = "🌖"
  elif phase == "Last Quarter":
    phase = "🌗"
  elif phase == "Waning Crescent":
    phase = "🌘"
  else:
    print("Invalid moon phase")
  return phase
  
answer = moon_phase('New Moon')
print(answer)
