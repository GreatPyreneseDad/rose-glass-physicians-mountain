"""
Cultural Bridge - End-of-Life Communication Support
===================================================

Provides culturally-informed translation support for physician
communication with families from diverse backgrounds.

Initial implementation: Hindu/Indian cultural lens
Based on research on Hindu end-of-life beliefs and practices.

Author: Christopher MacGregor bin Joseph
Date: December 2025
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from enum import Enum


class DecisionMakingStyle(Enum):
    """Cultural approaches to medical decision making"""
    INDIVIDUAL_AUTONOMY = "individual"  # Western default
    FAMILY_COLLECTIVE = "family"  # South Asian, East Asian
    ELDER_DIRECTED = "elder"  # Patriarchal family structures
    COMMUNITY_CONSENSUS = "community"  # Some indigenous traditions
    RELIGIOUS_AUTHORITY = "religious"  # Deferred to spiritual leader


class DisclosurePreference(Enum):
    """Cultural preferences for truth-telling about prognosis"""
    FULL_DISCLOSURE = "full"  # Direct, complete information
    GRADUATED_DISCLOSURE = "graduated"  # Information in stages
    FAMILY_MEDIATED = "family_first"  # Family receives info first
    PROTECTIVE_NON_DISCLOSURE = "protective"  # Shield patient from prognosis
    PATIENT_CHOICE = "patient_choice"  # Let patient determine level


class DeathBeliefs(Enum):
    """Broad categories of death/afterlife beliefs"""
    REINCARNATION = "reincarnation"  # Hindu, Buddhist
    HEAVEN_HELL = "heaven_hell"  # Abrahamic traditions
    CONTINUATION = "continuation"  # Ancestor traditions
    FINALITY = "finality"  # Secular perspectives
    LIBERATION = "liberation"  # Moksha, Nirvana
    UNKNOWN = "unknown"


@dataclass
class CulturalProfile:
    """Profile of cultural factors affecting end-of-life communication"""
    tradition_name: str
    decision_style: DecisionMakingStyle
    disclosure_preference: DisclosurePreference
    death_beliefs: DeathBeliefs
    
    # Key concepts to understand
    important_concepts: List[str] = field(default_factory=list)
    
    # Communication guidance
    suggested_language: Dict[str, str] = field(default_factory=dict)
    avoid_language: List[str] = field(default_factory=list)
    
    # Ritual considerations
    end_of_life_rituals: List[str] = field(default_factory=list)
    ritual_timing: str = ""
    
    # Family dynamics
    key_family_roles: List[str] = field(default_factory=list)
    
    # Pain/suffering perspective
    suffering_beliefs: str = ""


# Pre-defined cultural profiles
HINDU_INDIAN_PROFILE = CulturalProfile(
    tradition_name="Hindu (Indian)",
    decision_style=DecisionMakingStyle.FAMILY_COLLECTIVE,
    disclosure_preference=DisclosurePreference.FAMILY_MEDIATED,
    death_beliefs=DeathBeliefs.REINCARNATION,
    
    important_concepts=[
        "Karma - accumulated effects of actions across lifetimes",
        "Dharma - righteous duty and ethical living",
        "Moksha - liberation from cycle of rebirth",
        "Samsara - cycle of death and rebirth",
        "Good death (sukmrityu) vs bad death",
        "Consciousness at time of death affects next life",
        "Family dharma - duties to perform last rites"
    ],
    
    suggested_language={
        "prognosis": "The illness is progressing beyond what medicine can reverse",
        "death_approaching": "The time may be coming for the soul's journey",
        "comfort_focus": "We can focus on keeping them comfortable and present",
        "family_role": "Your presence and prayers matter greatly now",
        "consciousness": "Maintaining clarity of mind is important to many families",
        "transition": "This is a transition, not an ending"
    },
    
    avoid_language=[
        "There's nothing more we can do",
        "We need to withdraw care",
        "Death is imminent",
        "We're giving up",
        "It's time to let go"
    ],
    
    end_of_life_rituals=[
        "Family may wish to read from holy texts (Bhagavad Gita)",
        "Sanctified water (Ganga jal) may be offered to lips",
        "Tulsi (holy basil) leaf may be placed on tongue",
        "Family may wish patient to be on floor (return to earth)",
        "Mantra recitation - focusing dying person's thoughts on God",
        "Many families prefer patient to die at home",
        "Lamp may be lit near patient's head",
        "Cremation is standard - body should be handled respectfully"
    ],
    
    ritual_timing="Rituals should ideally be performed before death; some families prefer to begin when death seems near",
    
    key_family_roles=[
        "Eldest son often has specific ritual duties",
        "Extended family may be involved in decisions",
        "Religious authority (pandit) may be consulted",
        "Family elders may coordinate with medical team"
    ],
    
    suffering_beliefs=(
        "Suffering may be understood through karma lens - not as punishment "
        "but as opportunity for spiritual growth and clearing of past karma. "
        "Some patients may prefer less pain medication to maintain consciousness. "
        "However, this varies greatly by individual and family. Always ask."
    )
)

GENERAL_SOUTH_ASIAN_PROFILE = CulturalProfile(
    tradition_name="South Asian (General)",
    decision_style=DecisionMakingStyle.FAMILY_COLLECTIVE,
    disclosure_preference=DisclosurePreference.FAMILY_MEDIATED,
    death_beliefs=DeathBeliefs.UNKNOWN,
    
    important_concepts=[
        "Family honor and collective well-being often prioritized",
        "Elder respect - decisions may defer to family elders",
        "Izzat (honor/reputation) may affect openness to discussing death",
        "Immigration context may affect support systems"
    ],
    
    suggested_language={
        "family_inclusion": "Who would you like to be involved in these discussions?",
        "respecting_structure": "We want to communicate in the way that works for your family",
        "elder_consultation": "Would your family like time to consult together?"
    },
    
    avoid_language=[
        "Assuming individual autonomy model",
        "Pressuring immediate decisions",
        "Discussing prognosis without checking family preferences"
    ],
    
    end_of_life_rituals=[],  # Varies significantly by religion
    ritual_timing="Ask family about timing and ritual needs",
    
    key_family_roles=[
        "Identify family spokesperson",
        "Ask about elder involvement preferences",
        "Understand who should receive information first"
    ],
    
    suffering_beliefs=(
        "Varies significantly by religious and family background. "
        "Ask: 'How does your family understand suffering and illness?'"
    )
)


class CulturalBridge:
    """
    Provides culturally-informed guidance for end-of-life communication.
    
    NOT a replacement for:
    - Asking the individual family about their preferences
    - Recognizing within-group variation
    - Cultural humility and ongoing learning
    
    This is a starting point for awareness, not a prescription.
    """
    
    def __init__(self):
        self.profiles: Dict[str, CulturalProfile] = {
            "hindu_indian": HINDU_INDIAN_PROFILE,
            "south_asian_general": GENERAL_SOUTH_ASIAN_PROFILE,
        }
        
        # Universal considerations regardless of culture
        self.universal_principles = [
            "Always ask the family about their specific preferences",
            "Within-group variation is as significant as between-group",
            "Immigration generation affects cultural adherence",
            "Individual beliefs may differ from assumed cultural norms",
            "Cultural humility means not assuming we understand",
            "Building relationship before crisis enables better communication"
        ]
    
    def get_profile(self, cultural_key: str) -> Optional[CulturalProfile]:
        """Get cultural profile by key"""
        return self.profiles.get(cultural_key.lower())
    
    def get_communication_guidance(self, 
                                   cultural_key: str,
                                   communication_context: str) -> Dict[str, any]:
        """
        Get guidance for a specific communication context.
        
        Args:
            cultural_key: Key for cultural profile
            communication_context: 'prognosis', 'goals_of_care', 'imminent_death'
        
        Returns:
            Dict with suggested approaches, language, and cautions
        """
        
        profile = self.get_profile(cultural_key)
        
        if not profile:
            return self._get_generic_guidance(communication_context)
        
        guidance = {
            "cultural_awareness": [],
            "suggested_approach": [],
            "suggested_language": [],
            "cautions": [],
            "questions_to_ask_family": [],
            "ritual_considerations": []
        }
        
        # Add cultural-specific guidance
        guidance["cultural_awareness"].extend([
            f"Decision-making style often: {profile.decision_style.value}",
            f"Disclosure preference may be: {profile.disclosure_preference.value}",
            f"Death beliefs context: {profile.death_beliefs.value}"
        ])
        
        if profile.important_concepts:
            guidance["cultural_awareness"].append(
                f"Key concepts: {', '.join(profile.important_concepts[:3])}"
            )
        
        # Context-specific guidance
        if communication_context == "prognosis":
            guidance = self._add_prognosis_guidance(guidance, profile)
        elif communication_context == "goals_of_care":
            guidance = self._add_goals_guidance(guidance, profile)
        elif communication_context == "imminent_death":
            guidance = self._add_imminent_death_guidance(guidance, profile)
        
        # Add universal principles
        guidance["critical_reminder"] = self.universal_principles[0]
        
        return guidance
    
    def _add_prognosis_guidance(self, 
                                guidance: Dict, 
                                profile: CulturalProfile) -> Dict:
        """Add prognosis-specific cultural guidance"""
        
        if profile.disclosure_preference == DisclosurePreference.FAMILY_MEDIATED:
            guidance["suggested_approach"].extend([
                "Consider meeting with family first before patient",
                "Ask: 'How does your family prefer to receive difficult news?'",
                "Allow family to determine how much patient is told"
            ])
            
            guidance["questions_to_ask_family"].extend([
                "Who should be involved in these discussions?",
                "How much information would you like your loved one to receive directly?",
                "What is the best way for us to communicate with your family?"
            ])
        
        if profile.suggested_language.get("prognosis"):
            guidance["suggested_language"].append(
                profile.suggested_language["prognosis"]
            )
        
        if profile.avoid_language:
            guidance["cautions"].extend([
                f"Consider avoiding: '{phrase}'" for phrase in profile.avoid_language[:3]
            ])
        
        return guidance
    
    def _add_goals_guidance(self, 
                           guidance: Dict, 
                           profile: CulturalProfile) -> Dict:
        """Add goals of care discussion guidance"""
        
        if profile.decision_style == DecisionMakingStyle.FAMILY_COLLECTIVE:
            guidance["suggested_approach"].extend([
                "Allow time for family consultation before decisions",
                "Ask about family hierarchy and who should be in the room",
                "Understand that decisions may take longer than Western model expects"
            ])
        
        if profile.key_family_roles:
            guidance["suggested_approach"].append(
                f"Key roles to be aware of: {', '.join(profile.key_family_roles[:2])}"
            )
        
        if profile.suffering_beliefs:
            guidance["cultural_awareness"].append(
                f"Perspective on suffering: {profile.suffering_beliefs[:200]}..."
            )
            guidance["questions_to_ask_family"].append(
                "How does your family understand suffering and what gives comfort?"
            )
        
        return guidance
    
    def _add_imminent_death_guidance(self, 
                                    guidance: Dict, 
                                    profile: CulturalProfile) -> Dict:
        """Add imminent death communication guidance"""
        
        if profile.end_of_life_rituals:
            guidance["ritual_considerations"].extend(profile.end_of_life_rituals[:5])
            guidance["suggested_approach"].append(
                "Ask family about ritual preferences early enough to accommodate"
            )
        
        if profile.ritual_timing:
            guidance["ritual_considerations"].append(
                f"Timing note: {profile.ritual_timing}"
            )
        
        if profile.suggested_language.get("death_approaching"):
            guidance["suggested_language"].append(
                profile.suggested_language["death_approaching"]
            )
        
        if profile.suggested_language.get("transition"):
            guidance["suggested_language"].append(
                profile.suggested_language["transition"]
            )
        
        # Pain management considerations
        guidance["questions_to_ask_family"].extend([
            "What are your wishes regarding pain medication?",
            "How important is it for your loved one to be alert?",
            "Are there specific prayers or rituals you would like to perform?"
        ])
        
        return guidance
    
    def _get_generic_guidance(self, context: str) -> Dict[str, any]:
        """Get generic guidance when no cultural profile available"""
        
        return {
            "cultural_awareness": [
                "No specific cultural profile - approach with cultural humility"
            ],
            "suggested_approach": [
                "Ask about family preferences before assuming communication style",
                "Inquire about religious or spiritual needs",
                "Ask who should be involved in discussions and decisions"
            ],
            "suggested_language": [],
            "cautions": [
                "Don't assume Western individual autonomy model",
                "Don't assume patient wants full direct disclosure"
            ],
            "questions_to_ask_family": [
                "How does your family prefer to make medical decisions together?",
                "Are there cultural or religious considerations we should know about?",
                "Who would you like to be present for important discussions?"
            ],
            "ritual_considerations": [
                "Ask about any end-of-life rituals that are important to the family"
            ],
            "critical_reminder": self.universal_principles[0]
        }
    
    def list_available_profiles(self) -> List[str]:
        """List available cultural profiles"""
        return list(self.profiles.keys())
    
    def get_key_questions_for_any_family(self) -> List[str]:
        """
        Universal questions to ask any family, regardless of assumed background.
        
        These should be asked before assuming cultural patterns.
        """
        return [
            "How does your family prefer to make important medical decisions together?",
            "Who would you like to be included in discussions about your loved one's care?",
            "Are there cultural, religious, or spiritual practices that are important to your family?",
            "How much information would you/your family like about what to expect?",
            "Are there specific things that would bring comfort or have meaning for your family?",
            "Is there anything about your family's beliefs about illness or death we should understand?",
            "How can we best support you during this time?"
        ]
    
    def get_humility_reminders(self) -> List[str]:
        """Reminders about the limits of cultural knowledge"""
        return [
            "Cultural profiles describe tendencies, not certainties",
            "Individual variation within cultures exceeds between-culture variation",
            "Second/third generation immigrants may hold different views than parents",
            "Assuming cultural patterns without asking can cause harm",
            "Building trust relationship enables better cultural navigation",
            "When uncertain, ask - most families appreciate the effort",
            "Our own cultural lens affects how we perceive others"
        ]
