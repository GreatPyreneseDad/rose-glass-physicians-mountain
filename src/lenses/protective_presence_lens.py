"""
Protective Presence Lens
========================

Distinguishes between:
- Healthy protective distancing (sustainable practice)
- Maladaptive detachment (crisis indicator)

Based on research showing that "becoming a little numb to death"
can be adaptive when genuine compassion remains accessible.

Author: Christopher MacGregor bin Joseph
Date: December 2025
"""

from dataclasses import dataclass
from typing import List
from enum import Enum


class PresenceMode(Enum):
    """Mode of professional presence"""
    FULL_PRESENCE = "full_presence"
    PROTECTIVE_DISTANCE = "protective_distance"  # Healthy
    ADAPTIVE_NUMBING = "adaptive_numbing"  # Can be healthy
    PROBLEMATIC_DETACHMENT = "problematic_detachment"  # Concerning
    COMPLETE_DISCONNECT = "complete_disconnect"  # Crisis


@dataclass
class PresenceLensResult:
    """Result of viewing through protective presence lens"""
    mode: PresenceMode
    presence_when_needed: float  # Can they access presence when needed?
    protective_function: float  # Is distance serving protection?
    connection_preserved: float  # Is genuine connection still possible?
    
    interpretation: str
    health_assessment: str
    accessibility_note: str
    recommendations: List[str]


class ProtectivePresenceLens:
    """
    Lens for assessing quality of professional distancing.
    
    Key insight: Some emotional distance from patient deaths is
    necessary for sustainable practice. The question is whether
    the distance serves protection while preserving capacity for
    genuine connection when needed.
    
    "The skill of becoming a little numb to death" (Robert Lifton)
    can be adaptive when it allows continued compassionate service
    rather than representing loss of capacity for connection.
    """
    
    def __init__(self):
        self.name = "Protective Presence Lens"
        
        # Markers of full presence
        self.presence_markers = [
            'present', 'connected', 'felt', 'moved', 'touched',
            'tears', 'cried', 'heart', 'soul', 'deep'
        ]
        
        # Markers of protective distance
        self.distance_markers = [
            'professional', 'clinical', 'objective', 'boundary',
            'separate', 'step back', 'perspective'
        ]
        
        # Markers of healthy adaptation
        self.adaptive_markers = [
            'manage', 'cope', 'sustainable', 'continue', 'carry on',
            'find a way', 'learned to', 'balance'
        ]
        
        # Markers of problematic detachment
        self.detachment_markers = [
            'don\'t feel', 'numb', 'empty', 'nothing', 'detached',
            'disconnected', 'can\'t connect', 'going through motions'
        ]
        
        # Markers of preserved connection capacity
        self.connection_capacity = [
            'when needed', 'for the family', 'with patients',
            'genuine', 'authentic', 'real', 'care', 'matter'
        ]
    
    def view(self, text: str) -> PresenceLensResult:
        """View text through protective presence lens"""
        
        text_lower = text.lower()
        word_count = len(text.split())
        
        if word_count == 0:
            return self._empty_result()
        
        # Calculate dimensions
        presence_level = self._calculate_presence(text_lower, word_count)
        distance_level = self._calculate_distance(text_lower, word_count)
        adaptation_level = self._calculate_adaptation(text_lower, word_count)
        detachment_level = self._calculate_detachment(text_lower, word_count)
        connection_level = self._calculate_connection_capacity(text_lower, word_count)
        
        # Determine mode
        mode = self._determine_mode(
            presence_level, distance_level, 
            adaptation_level, detachment_level, connection_level
        )
        
        # Calculate key metrics
        presence_when_needed = self._assess_presence_accessibility(
            presence_level, connection_level, detachment_level
        )
        protective_function = self._assess_protective_function(
            distance_level, adaptation_level, detachment_level
        )
        connection_preserved = connection_level
        
        # Generate narrative
        interpretation = self._generate_interpretation(mode)
        health_assessment = self._assess_health(mode, protective_function, connection_preserved)
        accessibility_note = self._generate_accessibility_note(presence_when_needed)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(mode)
        
        return PresenceLensResult(
            mode=mode,
            presence_when_needed=presence_when_needed,
            protective_function=protective_function,
            connection_preserved=connection_preserved,
            interpretation=interpretation,
            health_assessment=health_assessment,
            accessibility_note=accessibility_note,
            recommendations=recommendations
        )
    
    def _calculate_presence(self, text: str, word_count: int) -> float:
        """Calculate presence markers"""
        count = sum(1 for m in self.presence_markers if m in text)
        return min(count / (word_count * 0.05 + 1), 1.0)
    
    def _calculate_distance(self, text: str, word_count: int) -> float:
        """Calculate distance markers"""
        count = sum(1 for m in self.distance_markers if m in text)
        return min(count / (word_count * 0.05 + 1), 1.0)
    
    def _calculate_adaptation(self, text: str, word_count: int) -> float:
        """Calculate adaptive coping markers"""
        count = sum(1 for m in self.adaptive_markers if m in text)
        return min(count / (word_count * 0.05 + 1), 1.0)
    
    def _calculate_detachment(self, text: str, word_count: int) -> float:
        """Calculate problematic detachment markers"""
        count = sum(1 for m in self.detachment_markers if m in text)
        return min(count / (word_count * 0.05 + 1), 1.0)
    
    def _calculate_connection_capacity(self, text: str, word_count: int) -> float:
        """Calculate preserved connection capacity"""
        count = sum(1 for m in self.connection_capacity if m in text)
        return min(count / (word_count * 0.05 + 1), 1.0)
    
    def _determine_mode(self, 
                       presence: float,
                       distance: float,
                       adaptation: float,
                       detachment: float,
                       connection: float) -> PresenceMode:
        """Determine current presence mode"""
        
        # Complete disconnect: high detachment, no connection capacity
        if detachment > 0.6 and connection < 0.2:
            return PresenceMode.COMPLETE_DISCONNECT
        
        # Problematic detachment: high detachment, low adaptation
        if detachment > 0.4 and adaptation < 0.3:
            return PresenceMode.PROBLEMATIC_DETACHMENT
        
        # Adaptive numbing: some detachment but with adaptation and connection
        if detachment > 0.2 and adaptation > 0.3 and connection > 0.3:
            return PresenceMode.ADAPTIVE_NUMBING
        
        # Protective distance: distance with connection preserved
        if distance > 0.3 and connection > 0.3 and detachment < 0.3:
            return PresenceMode.PROTECTIVE_DISTANCE
        
        # Full presence: high presence, low distance/detachment
        if presence > 0.4 and detachment < 0.2:
            return PresenceMode.FULL_PRESENCE
        
        return PresenceMode.PROTECTIVE_DISTANCE  # Default
    
    def _assess_presence_accessibility(self,
                                       presence: float,
                                       connection: float,
                                       detachment: float) -> float:
        """Assess whether presence is accessible when needed"""
        # High connection capacity + low detachment = accessible
        accessibility = (connection + (1 - detachment)) / 2
        # Presence level also contributes
        return (accessibility + presence) / 2
    
    def _assess_protective_function(self,
                                    distance: float,
                                    adaptation: float,
                                    detachment: float) -> float:
        """Assess whether distance is serving protective function"""
        # Distance + adaptation - detachment
        # Protective = distance that helps, not distance that harms
        protection = (distance + adaptation - detachment * 0.5) / 2
        return max(0.0, min(1.0, protection))
    
    def _generate_interpretation(self, mode: PresenceMode) -> str:
        """Generate interpretation of current mode"""
        
        interpretations = {
            PresenceMode.FULL_PRESENCE: (
                "Operating with full emotional presence. This allows deep "
                "connection but requires attention to sustainability and "
                "adequate recovery practices."
            ),
            PresenceMode.PROTECTIVE_DISTANCE: (
                "Maintaining professional distance while preserving capacity "
                "for genuine connection. This is often the sustainable mode "
                "for long-term practice in oncology."
            ),
            PresenceMode.ADAPTIVE_NUMBING: (
                "Some emotional numbing present but appears to be serving "
                "adaptive function. This 'little bit numb to death' can be "
                "protective if genuine connection remains accessible."
            ),
            PresenceMode.PROBLEMATIC_DETACHMENT: (
                "Detachment patterns may be affecting capacity for connection. "
                "This could indicate burnout precursors or compassion fatigue. "
                "Consider whether this is chosen distance or forced withdrawal."
            ),
            PresenceMode.COMPLETE_DISCONNECT: (
                "Significant disconnection detected. This may indicate crisis "
                "state requiring attention. This is not failure—it's a signal "
                "that the system needs care."
            )
        }
        
        return interpretations.get(mode, "Mode requires further analysis.")
    
    def _assess_health(self, 
                      mode: PresenceMode, 
                      protection: float, 
                      connection: float) -> str:
        """Assess health of current presence mode"""
        
        if mode in [PresenceMode.FULL_PRESENCE, PresenceMode.PROTECTIVE_DISTANCE]:
            return (
                "Current mode appears healthy and sustainable. "
                f"Protection function: {protection:.0%}, "
                f"Connection preserved: {connection:.0%}"
            )
        
        if mode == PresenceMode.ADAPTIVE_NUMBING:
            if connection > 0.4:
                return (
                    "Numbing appears adaptive—connection capacity preserved. "
                    "Monitor for further detachment."
                )
            else:
                return (
                    "Numbing may be shifting toward problematic detachment. "
                    "Connection capacity showing strain."
                )
        
        if mode == PresenceMode.PROBLEMATIC_DETACHMENT:
            return (
                "Current mode may not be sustainable. "
                "Consider support to restore connection capacity."
            )
        
        return (
            "Crisis state indicated. Immediate support warranted. "
            "This is a signal, not a character flaw."
        )
    
    def _generate_accessibility_note(self, accessibility: float) -> str:
        """Generate note about presence accessibility"""
        
        if accessibility > 0.7:
            return (
                "Genuine presence appears accessible when needed. "
                "Can access emotional connection for patients and families."
            )
        elif accessibility > 0.4:
            return (
                "Moderate presence accessibility. May require effort to "
                "access genuine connection in some situations."
            )
        else:
            return (
                "Presence accessibility appears limited. "
                "May benefit from support to restore connection capacity."
            )
    
    def _generate_recommendations(self, mode: PresenceMode) -> List[str]:
        """Generate mode-specific recommendations"""
        
        recommendations = {
            PresenceMode.FULL_PRESENCE: [
                "Ensure adequate recovery practices to sustain this presence",
                "Monitor for signs of over-extension or compassion fatigue",
                "This mode is valuable but requires self-care to maintain"
            ],
            PresenceMode.PROTECTIVE_DISTANCE: [
                "Current mode appears sustainable—continue practices",
                "Periodically check that connection remains accessible",
                "This balance serves both you and your patients"
            ],
            PresenceMode.ADAPTIVE_NUMBING: [
                "Monitor whether numbing remains adaptive or shifts further",
                "Ensure genuine connection remains accessible when needed",
                "Consider whether recovery practices are adequate"
            ],
            PresenceMode.PROBLEMATIC_DETACHMENT: [
                "Consider whether this is chosen distance or forced withdrawal",
                "Support may help restore connection capacity",
                "This pattern often responds to dedicated intervention"
            ],
            PresenceMode.COMPLETE_DISCONNECT: [
                "This is a crisis signal—please seek support",
                "Professional resources specifically for physician wellbeing exist",
                "Taking time for restoration is not abandonment"
            ]
        }
        
        return recommendations.get(mode, ["Monitor and reassess"])
    
    def _empty_result(self) -> PresenceLensResult:
        """Return result for empty input"""
        return PresenceLensResult(
            mode=PresenceMode.PROTECTIVE_DISTANCE,
            presence_when_needed=0.0,
            protective_function=0.0,
            connection_preserved=0.0,
            interpretation="No text to analyze",
            health_assessment="Insufficient data",
            accessibility_note="Cannot assess",
            recommendations=[]
        )
