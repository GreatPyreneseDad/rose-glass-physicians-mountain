"""
Cultural Bridge Lens
====================

Lens for viewing physician-family communication through
cultural context awareness.

Helps physicians recognize when their communication style
may need adaptation for different cultural frameworks.

Author: Christopher MacGregor bin Joseph
Date: December 2025
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from ..core.cultural_bridge import CulturalBridge, CulturalProfile


@dataclass
class CulturalTranslation:
    """Result of viewing communication through cultural lens"""
    detected_assumptions: List[str]
    cultural_considerations: List[str]
    suggested_adaptations: List[str]
    questions_to_explore: List[str]
    humility_reminder: str


class CulturalBridgeLens:
    """
    Lens for detecting cultural assumptions in communication.
    
    Helps physicians recognize Western-default assumptions
    and consider alternative cultural frameworks.
    """
    
    def __init__(self):
        self.name = "Cultural Bridge Lens"
        self.bridge = CulturalBridge()
        
        # Markers of Western assumptions
        self.autonomy_markers = [
            'your decision', 'you should decide', 'what do you want',
            'it\'s up to you', 'your choice', 'your right'
        ]
        
        self.direct_disclosure_markers = [
            'i need to tell you', 'you should know', 'the truth is',
            'honestly', 'frankly', 'you have to understand'
        ]
        
        self.time_pressure_markers = [
            'we need to decide', 'time is important', 'quickly',
            'right away', 'immediately', 'can\'t wait'
        ]
    
    def view(self, 
             text: str,
             cultural_context: Optional[str] = None) -> CulturalTranslation:
        """
        View communication through cultural bridge lens.
        
        Args:
            text: Communication to analyze
            cultural_context: Optional specific cultural context key
        
        Returns:
            CulturalTranslation with considerations and adaptations
        """
        
        text_lower = text.lower()
        
        # Detect assumptions
        assumptions = self._detect_assumptions(text_lower)
        
        # Get considerations based on context
        if cultural_context:
            profile = self.bridge.get_profile(cultural_context)
            considerations = self._get_specific_considerations(profile)
            adaptations = self._get_specific_adaptations(profile, assumptions)
        else:
            considerations = self._get_general_considerations()
            adaptations = self._get_general_adaptations(assumptions)
        
        # Generate questions
        questions = self.bridge.get_key_questions_for_any_family()[:4]
        
        # Humility reminder
        reminder = (
            "These are possibilities to consider, not cultural diagnoses. "
            "The family's actual preferences can only be learned by asking them."
        )
        
        return CulturalTranslation(
            detected_assumptions=assumptions,
            cultural_considerations=considerations,
            suggested_adaptations=adaptations,
            questions_to_explore=questions,
            humility_reminder=reminder
        )
    
    def _detect_assumptions(self, text: str) -> List[str]:
        """Detect Western cultural assumptions in communication"""
        
        assumptions = []
        
        # Individual autonomy assumption
        autonomy_count = sum(1 for m in self.autonomy_markers if m in text)
        if autonomy_count > 0:
            assumptions.append(
                "Assumption of individual autonomous decision-making. "
                "Many cultures use family-collective or elder-directed models."
            )
        
        # Direct disclosure assumption
        direct_count = sum(1 for m in self.direct_disclosure_markers if m in text)
        if direct_count > 0:
            assumptions.append(
                "Assumption that direct disclosure to patient is preferred. "
                "Some cultures prefer family-mediated or graduated disclosure."
            )
        
        # Time pressure assumption
        time_count = sum(1 for m in self.time_pressure_markers if m in text)
        if time_count > 0:
            assumptions.append(
                "Time pressure in decision-making. "
                "Family consultation may require more time in collective cultures."
            )
        
        if not assumptions:
            assumptions.append(
                "No obvious cultural assumptions detected in this sample, "
                "but cultural sensitivity should remain active."
            )
        
        return assumptions
    
    def _get_specific_considerations(self, 
                                    profile: Optional[CulturalProfile]) -> List[str]:
        """Get considerations for specific cultural context"""
        
        if not profile:
            return self._get_general_considerations()
        
        considerations = [
            f"Cultural context: {profile.tradition_name}",
            f"Typical decision style: {profile.decision_style.value}",
            f"Disclosure preference often: {profile.disclosure_preference.value}"
        ]
        
        if profile.key_family_roles:
            considerations.append(
                f"Key roles: {', '.join(profile.key_family_roles[:2])}"
            )
        
        if profile.suffering_beliefs:
            considerations.append(
                f"Suffering context: {profile.suffering_beliefs[:100]}..."
            )
        
        return considerations
    
    def _get_general_considerations(self) -> List[str]:
        """Get general cultural considerations"""
        
        return [
            "Cultural context not specified—consider asking family preferences",
            "Decision-making style may be individual, family, or elder-directed",
            "Disclosure preferences vary—ask before assuming direct disclosure",
            "Time frames for decisions may need flexibility for family consultation"
        ]
    
    def _get_specific_adaptations(self, 
                                 profile: Optional[CulturalProfile],
                                 assumptions: List[str]) -> List[str]:
        """Get specific adaptations for cultural context"""
        
        if not profile:
            return self._get_general_adaptations(assumptions)
        
        adaptations = []
        
        if profile.decision_style.value == "family":
            adaptations.append(
                "Consider inviting family members to discussions first"
            )
        
        if profile.disclosure_preference.value == "family_first":
            adaptations.append(
                "Ask family about disclosure preferences before discussing "
                "prognosis directly with patient"
            )
        
        if profile.suggested_language:
            for context, language in list(profile.suggested_language.items())[:2]:
                adaptations.append(f"Consider: '{language}'")
        
        if profile.avoid_language:
            for avoid in profile.avoid_language[:2]:
                adaptations.append(f"Consider avoiding: '{avoid}'")
        
        return adaptations
    
    def _get_general_adaptations(self, assumptions: List[str]) -> List[str]:
        """Get general adaptations based on detected assumptions"""
        
        adaptations = []
        
        if any('autonomy' in a.lower() for a in assumptions):
            adaptations.append(
                "Consider asking: 'How does your family make important decisions together?'"
            )
        
        if any('disclosure' in a.lower() for a in assumptions):
            adaptations.append(
                "Consider asking: 'How would you like to receive information "
                "about your loved one's condition?'"
            )
        
        if any('time' in a.lower() for a in assumptions):
            adaptations.append(
                "Consider offering: 'Would your family like time to consult "
                "before making this decision?'"
            )
        
        adaptations.append(
            "Build relationship before crisis—ask about preferences early"
        )
        
        return adaptations
