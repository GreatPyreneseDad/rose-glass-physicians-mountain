"""
Compassion Preservation Lens
============================

Detects patterns distinguishing:
- Compassion presence (sustainable engagement)
- Compassion fatigue (traumatic stress symptoms)
- Protective distancing (healthy boundary)
- Burnout precursors (energy depletion)

Based on ASCO research distinguishing burnout from compassion fatigue,
and Back et al.'s work on sustainable compassion in oncology.

Author: Christopher MacGregor bin Joseph
Date: December 2025
"""

from dataclasses import dataclass
from typing import List, Optional, Dict
from enum import Enum


class CompassionMode(Enum):
    """Current compassion operating mode"""
    FULL_ENGAGEMENT = "full_engagement"
    SUSTAINABLE_RHYTHM = "sustainable_rhythm"
    PROTECTIVE_DISTANCE = "protective_distance"
    COMPASSION_FATIGUE = "compassion_fatigue"
    BURNOUT_CASCADE = "burnout_cascade"


@dataclass
class CompassionAssessment:
    """Assessment of compassion state through this lens"""
    mode: CompassionMode
    mode_confidence: float
    
    # Component analyses
    engagement_level: float  # How emotionally present
    boundary_health: float  # Quality of professional boundaries
    recovery_capacity: float  # Ability to restore after encounters
    traumatic_intrusion: float  # Level of intrusive symptoms
    
    # Narrative
    pattern_description: str
    sustainability_assessment: str
    
    # Recommendations
    recommendations: List[str]
    warning_signs: List[str]


class CompassionPreservationLens:
    """
    Lens for assessing compassion sustainability in clinical practice.
    
    Key insight from research: compassion fatigue is distinct from burnout.
    - Burnout = chronic workplace stress leading to exhaustion/cynicism
    - Compassion fatigue = secondary traumatic stress from caring for traumatized
    
    This lens helps distinguish between them and identify when
    protective distance becomes problematic detachment.
    """
    
    def __init__(self):
        self.name = "Compassion Preservation Lens"
        
        # Vocabulary calibrations
        self.fatigue_markers = [
            'can\'t stop thinking', 'nightmares', 'intrusive', 'haunted',
            'triggered', 'flashback', 'images', 'won\'t leave', 'keeps coming back'
        ]
        
        self.burnout_markers = [
            'exhausted', 'empty', 'going through motions', 'don\'t care',
            'what\'s the point', 'mechanical', 'cynical', 'jaded'
        ]
        
        self.presence_markers = [
            'present', 'connected', 'honored', 'privilege', 'meaningful',
            'rewarding', 'grateful', 'touched'
        ]
        
        self.distance_markers = [
            'professional', 'boundary', 'separate', 'clinical',
            'detached', 'objective', 'distance'
        ]
        
        self.recovery_markers = [
            'rest', 'restored', 'recharged', 'supported', 'processed',
            'talked', 'shared', 'cried', 'grieved'
        ]
    
    def assess(self, text: str, 
               context: Optional[Dict] = None) -> CompassionAssessment:
        """
        Assess compassion state from physician expression.
        
        Args:
            text: Physician expression to analyze
            context: Optional context (specialty, recent_losses, etc.)
        
        Returns:
            CompassionAssessment with mode and recommendations
        """
        
        text_lower = text.lower()
        word_count = len(text.split())
        
        if word_count == 0:
            return self._empty_assessment()
        
        # Calculate component scores
        engagement_level = self._calculate_engagement(text_lower, word_count)
        boundary_health = self._calculate_boundary_health(text_lower, word_count)
        recovery_capacity = self._calculate_recovery(text_lower, word_count)
        traumatic_intrusion = self._calculate_intrusion(text_lower, word_count)
        
        # Determine mode
        mode, confidence = self._determine_mode(
            engagement_level, boundary_health, 
            recovery_capacity, traumatic_intrusion
        )
        
        # Generate narrative
        pattern_desc = self._generate_pattern_description(
            mode, engagement_level, boundary_health
        )
        sustainability = self._assess_sustainability(
            mode, recovery_capacity, traumatic_intrusion
        )
        
        # Generate recommendations
        recommendations = self._generate_recommendations(mode)
        warning_signs = self._identify_warning_signs(
            mode, traumatic_intrusion, recovery_capacity
        )
        
        return CompassionAssessment(
            mode=mode,
            mode_confidence=confidence,
            engagement_level=engagement_level,
            boundary_health=boundary_health,
            recovery_capacity=recovery_capacity,
            traumatic_intrusion=traumatic_intrusion,
            pattern_description=pattern_desc,
            sustainability_assessment=sustainability,
            recommendations=recommendations,
            warning_signs=warning_signs
        )
    
    def _calculate_engagement(self, text: str, word_count: int) -> float:
        """Calculate emotional engagement level"""
        presence_count = sum(1 for m in self.presence_markers if m in text)
        burnout_count = sum(1 for m in self.burnout_markers if m in text)
        
        # Presence markers increase, burnout decreases
        base_score = 0.5
        presence_boost = min(presence_count * 0.15, 0.4)
        burnout_penalty = min(burnout_count * 0.15, 0.4)
        
        return max(0.0, min(1.0, base_score + presence_boost - burnout_penalty))
    
    def _calculate_boundary_health(self, text: str, word_count: int) -> float:
        """Calculate professional boundary health"""
        distance_count = sum(1 for m in self.distance_markers if m in text)
        over_involvement = ['too much', 'can\'t let go', 'my patient', 'felt like mine']
        over_count = sum(1 for m in over_involvement if m in text)
        
        # Some distance is healthy; too much or too little is concerning
        if distance_count >= 1 and over_count == 0:
            return 0.7  # Healthy awareness of boundaries
        elif over_count > 0:
            return 0.3  # Over-involvement concerns
        elif distance_count >= 3:
            return 0.4  # May be too distant
        else:
            return 0.5  # Neutral
    
    def _calculate_recovery(self, text: str, word_count: int) -> float:
        """Calculate recovery capacity indicators"""
        recovery_count = sum(1 for m in self.recovery_markers if m in text)
        
        return min(recovery_count * 0.2, 0.8) + 0.1
    
    def _calculate_intrusion(self, text: str, word_count: int) -> float:
        """Calculate level of traumatic intrusion symptoms"""
        fatigue_count = sum(1 for m in self.fatigue_markers if m in text)
        
        # Higher score = more intrusion symptoms
        return min(fatigue_count * 0.2, 1.0)
    
    def _determine_mode(self, 
                       engagement: float,
                       boundary: float,
                       recovery: float,
                       intrusion: float) -> tuple:
        """Determine current compassion operating mode"""
        
        # Compassion fatigue: high intrusion symptoms
        if intrusion > 0.5:
            confidence = min(intrusion, 0.8)
            return (CompassionMode.COMPASSION_FATIGUE, confidence)
        
        # Burnout cascade: low engagement, low recovery
        if engagement < 0.3 and recovery < 0.3:
            return (CompassionMode.BURNOUT_CASCADE, 0.7)
        
        # Protective distance: deliberate boundaries, moderate engagement
        if boundary >= 0.6 and engagement >= 0.3 and engagement <= 0.7:
            return (CompassionMode.PROTECTIVE_DISTANCE, 0.6)
        
        # Full engagement: high engagement, good recovery
        if engagement > 0.7 and recovery > 0.4:
            return (CompassionMode.FULL_ENGAGEMENT, 0.7)
        
        # Default: sustainable rhythm
        return (CompassionMode.SUSTAINABLE_RHYTHM, 0.5)
    
    def _generate_pattern_description(self, 
                                     mode: CompassionMode,
                                     engagement: float,
                                     boundary: float) -> str:
        """Generate narrative description of pattern"""
        
        descriptions = {
            CompassionMode.FULL_ENGAGEMENT: (
                "High emotional engagement with patients and families. "
                f"Engagement level: {engagement:.0%}. "
                "This can be deeply rewarding but requires attention to sustainability."
            ),
            CompassionMode.SUSTAINABLE_RHYTHM: (
                "Balanced engagement pattern detected. "
                "Emotional presence appears sustainable with current practices."
            ),
            CompassionMode.PROTECTIVE_DISTANCE: (
                "Healthy professional boundaries evident. "
                "This 'becoming a little numb to death' can be adaptive when "
                "genuine compassion remains accessible when needed."
            ),
            CompassionMode.COMPASSION_FATIGUE: (
                "Patterns suggest secondary traumatic stress may be present. "
                "Intrusive symptoms indicate the work may be affecting you "
                "in ways that deserve attention and support."
            ),
            CompassionMode.BURNOUT_CASCADE: (
                "Patterns suggest energy depletion and diminished engagement. "
                "This is a signal, not a failure. "
                "The system is indicating need for restoration."
            )
        }
        
        return descriptions.get(mode, "Pattern requires additional context.")
    
    def _assess_sustainability(self, 
                              mode: CompassionMode,
                              recovery: float,
                              intrusion: float) -> str:
        """Assess sustainability of current pattern"""
        
        if mode in [CompassionMode.COMPASSION_FATIGUE, CompassionMode.BURNOUT_CASCADE]:
            return (
                "Current pattern appears unsustainable. "
                "Intervention or support may prevent deterioration."
            )
        
        if recovery < 0.3:
            return (
                "Recovery capacity appears limited. "
                "Current engagement may not be sustainable long-term."
            )
        
        if mode == CompassionMode.PROTECTIVE_DISTANCE and recovery > 0.4:
            return (
                "Current protective stance appears sustainable. "
                "Boundaries serving protective function while maintaining capacity."
            )
        
        if mode == CompassionMode.FULL_ENGAGEMENT and recovery > 0.5:
            return (
                "High engagement appears sustainable with current recovery practices. "
                "Continue practices that restore."
            )
        
        return "Sustainability assessment uncertain. Monitor over time."
    
    def _generate_recommendations(self, mode: CompassionMode) -> List[str]:
        """Generate mode-specific recommendations"""
        
        recs = {
            CompassionMode.FULL_ENGAGEMENT: [
                "Maintain practices that restore compassion reserves",
                "Monitor for signs of over-extension",
                "Ensure boundaries remain healthy alongside engagement"
            ],
            CompassionMode.SUSTAINABLE_RHYTHM: [
                "Current practices appear effective—continue",
                "Note what helps maintain this balance",
                "Share what works with colleagues who may be struggling"
            ],
            CompassionMode.PROTECTIVE_DISTANCE: [
                "This distance may be serving a protective function",
                "Check: Is genuine connection still accessible when needed?",
                "Ensure distance is chosen, not forced by depletion"
            ],
            CompassionMode.COMPASSION_FATIGUE: [
                "Secondary traumatic stress responds to specific interventions",
                "Consider speaking with someone trained in trauma support",
                "Processing rituals after difficult cases may help",
                "This is not weakness—it's the cost of caring work"
            ],
            CompassionMode.BURNOUT_CASCADE: [
                "Restoration needed before continued depletion",
                "Professional support specifically for physician burnout exists",
                "Time off is not abandonment—it's preservation of capacity to serve"
            ]
        }
        
        return recs.get(mode, ["Monitor and reassess"])
    
    def _identify_warning_signs(self, 
                               mode: CompassionMode,
                               intrusion: float,
                               recovery: float) -> List[str]:
        """Identify warning signs to monitor"""
        
        signs = []
        
        if intrusion > 0.3:
            signs.append("Intrusive thoughts about patients increasing")
        
        if recovery < 0.3:
            signs.append("Recovery practices not restoring reserves")
        
        if mode == CompassionMode.BURNOUT_CASCADE:
            signs.append("Cynicism or detachment affecting patient care")
            signs.append("Considering leaving medicine due to burnout")
        
        if mode == CompassionMode.COMPASSION_FATIGUE:
            signs.append("Nightmares or sleep disruption from work")
            signs.append("Avoiding certain patient types or situations")
        
        return signs
    
    def _empty_assessment(self) -> CompassionAssessment:
        """Return assessment for empty input"""
        return CompassionAssessment(
            mode=CompassionMode.SUSTAINABLE_RHYTHM,
            mode_confidence=0.0,
            engagement_level=0.0,
            boundary_health=0.0,
            recovery_capacity=0.0,
            traumatic_intrusion=0.0,
            pattern_description="No text to analyze",
            sustainability_assessment="Insufficient data",
            recommendations=[],
            warning_signs=[]
        )
