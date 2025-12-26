                "Informal peer support may be helpful",
                "Consider whether current workload matches recovery capacity"
            ])
        
        # State-specific suggestions
        reserve = state.get('compassion_reserve', 0.5)
        if reserve < 0.25:
            suggestions.append(
                "Compassion reserve very low. Prioritize restoration activities."
            )
        
        f_score = state.get('f', 0.5)
        if f_score < 0.2:
            suggestions.append(
                "Isolation compounds difficulty. Consider reaching out to someone "
                "who understands this work."
            )
        
        return suggestions
    
    def get_summary_for_period(self, start: datetime, end: datetime) -> Dict:
        """Get summary statistics for a time period"""
        
        points = [p for p in self.history 
                  if start <= p.timestamp <= end]
        
        if not points:
            return {"error": "No data in specified period"}
        
        return {
            "period": f"{start.date()} to {end.date()}",
            "data_points": len(points),
            "averages": {
                "psi": statistics.mean([p.psi for p in points]),
                "rho": statistics.mean([p.rho for p in points]),
                "q": statistics.mean([p.q for p in points]),
                "f": statistics.mean([p.f for p in points]),
                "compassion_reserve": statistics.mean([p.compassion_reserve for p in points]),
                "grief_load": statistics.mean([p.cumulative_grief_load for p in points])
            },
            "losses_recorded": sum(p.recent_losses for p in points)
        }
                "Consider what practices help restore compassion reserves",
                "Debrief support after difficult cases can help processing"
            ])
        
        # State-specific suggestions
        if state.get('compassion_reserve', 1.0) < 0.25:
            suggestions.append(
                "Compassion reserves critically low. "
                "Permission to prioritize self-care is not weakness."
            )
        
        if state.get('f', 1.0) < 0.2:
            suggestions.append(
                "Isolation compounds burden. "
                "Connection with others who understand this work may help."
            )
        
        return suggestions
    
    def get_timeline_summary(self, days: int = 90) -> str:
        """Get narrative summary of pattern over time"""
        
        recent = self.get_recent_points(days)
        
        if len(recent) < 5:
            return "Insufficient history for timeline summary."
        
        # Divide into periods
        period_length = len(recent) // 3
        early = recent[:period_length]
        middle = recent[period_length:2*period_length]
        late = recent[2*period_length:]
        
        def period_summary(points: List[TrackingPoint]) -> Dict[str, float]:
            return {
                'reserve': statistics.mean([p.compassion_reserve for p in points]),
                'load': statistics.mean([p.cumulative_grief_load for p in points]),
                'wisdom': statistics.mean([p.rho for p in points])
            }
        
        early_s = period_summary(early)
        late_s = period_summary(late)
        
        # Generate narrative
        reserve_change = "increased" if late_s['reserve'] > early_s['reserve'] else "decreased"
        load_change = "increased" if late_s['load'] > early_s['load'] else "decreased"
        wisdom_change = "increased" if late_s['wisdom'] > early_s['wisdom'] else "decreased"
        
        summary = f"""
Over the past {days} days:

• Compassion reserves have {reserve_change} from ~{early_s['reserve']:.0%} to ~{late_s['reserve']:.0%}
• Grief load has {load_change} from ~{early_s['load']:.0%} to ~{late_s['load']:.0%}  
• Wisdom accumulation has {wisdom_change} from ~{early_s['wisdom']:.0%} to ~{late_s['wisdom']:.0%}

"""
        
        # Interpretation
        if late_s['reserve'] < 0.3 and load_change == "increased":
            summary += (
                "Pattern suggests grief accumulation may be outpacing recovery. "
                "Consider whether current load matches capacity."
            )
        elif late_s['wisdom'] > early_s['wisdom'] and late_s['load'] < early_s['load']:
            summary += (
                "Positive transformation pattern: grief converting to wisdom, "
                "reserves rebuilding. Continue supportive practices."
            )
        else:
            summary += (
                "Mixed pattern. Some dimensions concerning, others stable or improving. "
                "See detailed trend analysis for specifics."
            )
        
        return summary
