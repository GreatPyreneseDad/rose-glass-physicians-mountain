"""
Physician Rose Glass - Core Translation Engine
==============================================

Extends Rose Glass v2.1 for physician-specific pattern translation,
particularly for those working with terminal illness.

Author: Christopher MacGregor bin Joseph
Date: December 2025
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime
from enum import Enum
import math


class ClinicalContext(Enum):
    """Clinical specialty contexts for lens calibration"""
    PEDIATRIC_ONCOLOGY = "pediatric_oncology"
    ADULT_ONCOLOGY = "adult_oncology"
    NEURO_ONCOLOGY = "neuro_oncology"
    HEMATOLOGY = "hematology"
    PALLIATIVE_CARE = "palliative_care"
    HOSPICE = "hospice"
    EMERGENCY = "emergency"
    ICU = "icu"
    GENERAL_ONCOLOGY = "general_oncology"


class CompassionState(Enum):
    """States of compassion presence"""
    FULL_PRESENCE = "full_presence"  # Engaged, connected, sustainable
    PROTECTIVE_DISTANCE = "protective_distance"  # Healthy boundary
    COMPASSION_FATIGUE = "compassion_fatigue"  # Traumatic stress present
    BURNOUT_PRECURSOR = "burnout_precursor"  # Energy depletion beginning
    CRISIS = "crisis"  # Immediate support needed


@dataclass
class PhysicianGCTVariables:
    """Extended GCT variables for physician context"""
    # Core four
    psi: float = 0.0  # Internal consistency - clinical self / human self integration
    rho: float = 0.0  # Accumulated wisdom - compressed grief into knowledge
    q: float = 0.0    # Moral activation - emotional engagement level
    f: float = 0.0    # Social belonging - clinical community connection
    
    # Extended dimensions
    tau: float = 0.0  # Temporal depth - pattern across patient losses
    lambda_coef: float = 0.0  # Lens interference - clinical vs personal frame ambiguity
    
    # Physician-specific derived measures
    wisdom_compression_ratio: float = 0.0  # How much grief has become accessible knowledge
    compassion_reserve: float = 0.0  # Available emotional capacity
    cumulative_grief_load: float = 0.0  # Unprocessed loss weight
    
    def to_dict(self) -> Dict[str, float]:
        return {
            'psi': self.psi,
            'rho': self.rho,
            'q': self.q,
            'f': self.f,
            'tau': self.tau,
            'lambda': self.lambda_coef,
            'wisdom_compression_ratio': self.wisdom_compression_ratio,
            'compassion_reserve': self.compassion_reserve,
            'cumulative_grief_load': self.cumulative_grief_load
        }


@dataclass
class PhysicianTranslation:
    """Result of translating physician expression through Rose Glass"""
    variables: PhysicianGCTVariables
    lens_used: str
    compassion_state: CompassionState
    
    # Narrative elements
    pattern_summary: str = ""
    wisdom_pathway: str = ""
    support_suggestions: List[str] = field(default_factory=list)
    cultural_considerations: List[str] = field(default_factory=list)
    
    # Uncertainty acknowledgment
    confidence: float = 0.0
    alternative_readings: List[str] = field(default_factory=list)
    uncertainty_notes: List[str] = field(default_factory=list)
    
    # Temporal tracking
    timestamp: datetime = field(default_factory=datetime.now)
    
    def get_narrative(self) -> str:
        """Generate human-readable narrative of translation"""
        narrative = f"""
╔══════════════════════════════════════════════════════════════════╗
║            ROSE GLASS PHYSICIAN TRANSLATION                       ║
╠══════════════════════════════════════════════════════════════════╣
║ Lens: {self.lens_used:50s}           ║
║ Compassion State: {self.compassion_state.value:42s}║
╠══════════════════════════════════════════════════════════════════╣
║ PATTERN DIMENSIONS (through this lens)                           ║
╠══════════════════════════════════════════════════════════════════╣
║ Ψ Clinical-Human Integration:    {self.variables.psi:.2f}                         ║
║ ρ Wisdom Accumulation:           {self.variables.rho:.2f}                         ║
║ q Emotional Engagement:          {self.variables.q:.2f}                         ║
║ f Community Connection:          {self.variables.f:.2f}                         ║
║ τ Temporal Pattern Depth:        {self.variables.tau:.2f}                         ║
║ λ Frame Ambiguity:               {self.variables.lambda_coef:.2f}                         ║
╠══════════════════════════════════════════════════════════════════╣
║ DERIVED INSIGHTS                                                 ║
╠══════════════════════════════════════════════════════════════════╣
║ Wisdom Compression:              {self.variables.wisdom_compression_ratio:.2f}                         ║
║ Compassion Reserve:              {self.variables.compassion_reserve:.2f}                         ║
║ Unprocessed Grief Load:          {self.variables.cumulative_grief_load:.2f}                         ║
╠══════════════════════════════════════════════════════════════════╣
║ Translation Confidence: {self.confidence:.0%}                                      ║
╚══════════════════════════════════════════════════════════════════╝

PATTERN SUMMARY:
{self.pattern_summary}

WISDOM PATHWAY:
{self.wisdom_pathway}
"""
        
        if self.support_suggestions:
            narrative += "\nSUPPORT CONSIDERATIONS:\n"
            for suggestion in self.support_suggestions:
                narrative += f"  • {suggestion}\n"
        
        if self.cultural_considerations:
            narrative += "\nCULTURAL BRIDGE NOTES:\n"
            for note in self.cultural_considerations:
                narrative += f"  • {note}\n"
        
        if self.alternative_readings:
            narrative += "\nALTERNATIVE READINGS:\n"
            for reading in self.alternative_readings:
                narrative += f"  → {reading}\n"
        
        if self.uncertainty_notes:
            narrative += "\nUNCERTAINTY NOTES:\n"
            for note in self.uncertainty_notes:
                narrative += f"  ⚠ {note}\n"
        
        return narrative


class BiologicalOptimizer:
    """
    Prevents extreme emotional activation using Michaelis-Menten kinetics.
    
    For physicians, this is crucial:
    - Too low q = detachment (can't connect with patients/families)
    - Too high q = overwhelm (can't function clinically)
    - Optimized q = sustainable compassion presence
    """
    
    def __init__(self, Km: float = 0.25, Ki: float = 1.5):
        self.Km = Km  # Half-saturation constant
        self.Ki = Ki  # Inhibition constant
    
    def optimize_q(self, q_raw: float) -> float:
        """Apply biological optimization to emotional activation"""
        if q_raw <= 0:
            return 0.0
        
        # Michaelis-Menten with substrate inhibition
        denominator = self.Km + q_raw + (q_raw ** 2) / self.Ki
        
        if denominator == 0:
            return 0.0
        
        return min(q_raw / denominator, 0.95)
    
    def calculate_compassion_reserve(self, q_current: float, 
                                     cumulative_load: float,
                                     days_since_rest: int = 0) -> float:
        """
        Estimate remaining compassion capacity.
        
        Based on the cumulative stress model from oncology research:
        each additional stressor depletes reserves.
        """
        base_reserve = 1.0 - self.optimize_q(q_current)
        load_depletion = min(cumulative_load * 0.15, 0.5)
        fatigue_factor = min(days_since_rest * 0.02, 0.3)
        
        reserve = max(base_reserve - load_depletion - fatigue_factor, 0.05)
        return reserve


class PhysicianPatternExtractor:
    """
    Extracts GCT variables from physician expressions.
    
    Calibrated for the unique patterns of medical professional communication:
    - Clinical detachment markers
    - Grief vocabulary
    - Burnout precursors
    - Meaning-making language
    """
    
    # Vocabulary calibrations
    CLINICAL_DETACHMENT_MARKERS = [
        'the patient', 'case', 'presented', 'expired', 'passed',
        'prognosis', 'outcome', 'treatment', 'protocol'
    ]
    
    HUMAN_CONNECTION_MARKERS = [
        'i', 'we', 'felt', 'feel', 'hard', 'difficult', 'tears',
        'family', 'mother', 'father', 'child', 'loved', 'miss'
    ]
    
    GRIEF_MARKERS = [
        'lost', 'death', 'died', 'passed', 'gone', 'miss',
        'another one', 'how many more', 'can\'t take', 'breaking'
    ]
    
    WISDOM_MARKERS = [
        'learned', 'understand', 'realize', 'meaning', 'purpose',
        'grateful', 'honored', 'privilege', 'taught me', 'gift'
    ]
    
    BURNOUT_PRECURSORS = [
        'exhausted', 'can\'t', 'don\'t care', 'what\'s the point',
        'numb', 'empty', 'mechanical', 'going through motions'
    ]
    
    COMPASSION_FATIGUE_MARKERS = [
        'nightmares', 'intrusive', 'can\'t stop thinking',
        'haunted', 'triggered', 'reminded', 'flashback'
    ]
    
    POST_TRAUMATIC_GROWTH_MARKERS = [
        'stronger', 'perspective', 'appreciate', 'relationship',
        'meaning', 'spiritual', 'growth', 'transformed'
    ]
    
    def extract(self, text: str) -> PhysicianGCTVariables:
        """Extract all variables from physician expression"""
        text_lower = text.lower()
        words = text_lower.split()
        word_count = len(words)
        
        if word_count == 0:
            return PhysicianGCTVariables()
        
        # Ψ - Clinical-Human Integration
        clinical_count = sum(1 for marker in self.CLINICAL_DETACHMENT_MARKERS 
                           if marker in text_lower)
        human_count = sum(1 for marker in self.HUMAN_CONNECTION_MARKERS 
                         if marker in text_lower)
        
        # High psi = both clinical and human present in balance
        clinical_ratio = clinical_count / (word_count * 0.1 + 1)
        human_ratio = human_count / (word_count * 0.1 + 1)
        psi = min((clinical_ratio + human_ratio) / 2 * 2, 1.0)
        
        # ρ - Wisdom Accumulation
        wisdom_count = sum(1 for marker in self.WISDOM_MARKERS 
                          if marker in text_lower)
        ptg_count = sum(1 for marker in self.POST_TRAUMATIC_GROWTH_MARKERS 
                       if marker in text_lower)
        rho = min((wisdom_count + ptg_count) / (word_count * 0.05 + 1), 1.0)
        
        # q - Emotional Engagement
        grief_count = sum(1 for marker in self.GRIEF_MARKERS 
                         if marker in text_lower)
        emotion_intensity = grief_count / (word_count * 0.05 + 1)
        
        # Check for suppression indicators
        has_suppression = 'held it together' in text_lower or 'stayed strong' in text_lower
        if has_suppression:
            emotion_intensity *= 1.5  # Suppressed emotion is still present
        
        q = min(emotion_intensity, 1.0)
        
        # f - Community Connection
        collective_markers = ['we', 'team', 'colleagues', 'nurses', 'staff']
        isolation_markers = ['alone', 'nobody', 'by myself', 'no one']
        
        collective_count = sum(1 for marker in collective_markers if marker in text_lower)
        isolation_count = sum(1 for marker in isolation_markers if marker in text_lower)
        
        f = min(collective_count / (word_count * 0.03 + 1), 1.0)
        if isolation_count > 0:
            f *= 0.5
        
        # τ - Temporal Depth
        temporal_markers = ['years', 'months', 'always', 'never', 'every time',
                          'another', 'again', 'keeps happening']
        temporal_count = sum(1 for marker in temporal_markers if marker in text_lower)
        tau = min(temporal_count / 3, 1.0)
        
        # λ - Frame Ambiguity
        # High λ when mixing clinical and personal frames
        lambda_coef = abs(clinical_ratio - human_ratio)
        
        # Derived measures
        burnout_count = sum(1 for marker in self.BURNOUT_PRECURSORS 
                          if marker in text_lower)
        fatigue_count = sum(1 for marker in self.COMPASSION_FATIGUE_MARKERS 
                           if marker in text_lower)
        
        # Wisdom compression ratio: how much grief has transformed
        raw_grief = grief_count + fatigue_count
        processed_wisdom = wisdom_count + ptg_count
        
        if raw_grief > 0:
            wisdom_compression_ratio = min(processed_wisdom / raw_grief, 1.0)
        else:
            wisdom_compression_ratio = 0.5  # No grief present to process
        
        cumulative_grief_load = min((grief_count + burnout_count + fatigue_count) / 
                                    (word_count * 0.05 + 1), 1.0)
        
        return PhysicianGCTVariables(
            psi=psi,
            rho=rho,
            q=q,
            f=f,
            tau=tau,
            lambda_coef=lambda_coef,
            wisdom_compression_ratio=wisdom_compression_ratio,
            compassion_reserve=0.0,  # Calculated separately with optimizer
            cumulative_grief_load=cumulative_grief_load
        )


class PhysicianRoseGlass:
    """
    Main translation engine for physician expressions.
    
    Transforms raw experience into pattern translations that:
    - Honor the reality of suffering without amplifying it
    - Identify pathways from grief to wisdom
    - Support without prescribing
    - Maintain cultural humility
    """
    
    def __init__(self, context: str = 'general_oncology'):
        self.context = ClinicalContext(context) if isinstance(context, str) else context
        self.extractor = PhysicianPatternExtractor()
        self.optimizer = BiologicalOptimizer()
        self.accumulation_history: List[PhysicianGCTVariables] = []
        
        # Context-specific calibrations
        self.context_calibrations = self._load_calibrations()
    
    def _load_calibrations(self) -> Dict[str, float]:
        """Load context-specific lens calibrations"""
        
        calibrations = {
            ClinicalContext.PEDIATRIC_ONCOLOGY: {
                'grief_weight': 1.3,  # Higher grief intensity expected
                'wisdom_acceleration': 0.8,  # Wisdom often slower to develop
                'compassion_baseline': 0.7,  # Higher compassion demands
            },
            ClinicalContext.PALLIATIVE_CARE: {
                'grief_weight': 1.0,
                'wisdom_acceleration': 1.2,  # More opportunity for meaning
                'compassion_baseline': 0.6,
            },
            ClinicalContext.GENERAL_ONCOLOGY: {
                'grief_weight': 1.0,
                'wisdom_acceleration': 1.0,
                'compassion_baseline': 0.5,
            }
        }
        
        return calibrations.get(self.context, calibrations[ClinicalContext.GENERAL_ONCOLOGY])
    
    def translate(self, text: str, 
                  lens: Optional[Any] = None,
                  track_accumulation: bool = True) -> PhysicianTranslation:
        """
        Translate physician expression through Rose Glass.
        
        Args:
            text: Raw expression (journal entry, reflection, etc.)
            lens: Specific lens to use (default: context-appropriate)
            track_accumulation: Whether to track over time
        
        Returns:
            PhysicianTranslation with pattern analysis and pathways
        """
        
        # Extract raw variables
        variables = self.extractor.extract(text)
        
        # Apply biological optimization to emotional activation
        variables.q = self.optimizer.optimize_q(variables.q)
        
        # Calculate compassion reserve
        variables.compassion_reserve = self.optimizer.calculate_compassion_reserve(
            variables.q,
            variables.cumulative_grief_load
        )
        
        # Track accumulation if enabled
        if track_accumulation:
            self.accumulation_history.append(variables)
        
        # Determine compassion state
        compassion_state = self._assess_compassion_state(variables)
        
        # Generate narrative elements
        pattern_summary = self._generate_pattern_summary(variables, compassion_state)
        wisdom_pathway = self._generate_wisdom_pathway(variables)
        support_suggestions = self._generate_support_suggestions(variables, compassion_state)
        
        # Calculate confidence
        confidence = self._calculate_confidence(variables, text)
        
        # Generate alternative readings
        alternative_readings = self._generate_alternatives(variables)
        
        return PhysicianTranslation(
            variables=variables,
            lens_used=lens.__class__.__name__ if lens else "Default Physician Lens",
            compassion_state=compassion_state,
            pattern_summary=pattern_summary,
            wisdom_pathway=wisdom_pathway,
            support_suggestions=support_suggestions,
            confidence=confidence,
            alternative_readings=alternative_readings,
            uncertainty_notes=self._generate_uncertainty_notes(variables)
        )
    
    def _assess_compassion_state(self, v: PhysicianGCTVariables) -> CompassionState:
        """Assess current compassion state from variables"""
        
        # High cumulative load + low reserve = crisis
        if v.cumulative_grief_load > 0.7 and v.compassion_reserve < 0.2:
            return CompassionState.CRISIS
        
        # Signs of compassion fatigue (traumatic stress symptoms)
        if v.q > 0.6 and v.wisdom_compression_ratio < 0.3:
            return CompassionState.COMPASSION_FATIGUE
        
        # Burnout precursors (exhaustion without processing)
        if v.cumulative_grief_load > 0.5 and v.rho < 0.3:
            return CompassionState.BURNOUT_PRECURSOR
        
        # Healthy protective distance
        if v.psi > 0.5 and v.q < 0.5 and v.compassion_reserve > 0.4:
            return CompassionState.PROTECTIVE_DISTANCE
        
        # Full presence
        return CompassionState.FULL_PRESENCE
    
    def _generate_pattern_summary(self, v: PhysicianGCTVariables, 
                                  state: CompassionState) -> str:
        """Generate narrative summary of detected patterns"""
        
        summaries = {
            CompassionState.FULL_PRESENCE: (
                f"Patterns suggest integration of clinical and human dimensions (Ψ={v.psi:.2f}). "
                f"Emotional engagement is present and sustainable (q={v.q:.2f}). "
                f"Compassion reserves appear adequate ({v.compassion_reserve:.0%})."
            ),
            CompassionState.PROTECTIVE_DISTANCE: (
                f"Patterns indicate healthy professional boundaries. "
                f"Clinical frame may be providing necessary protection. "
                f"This 'becoming a little numb to death' can be adaptive when sustained "
                f"compassion is also present."
            ),
            CompassionState.COMPASSION_FATIGUE: (
                f"Patterns suggest traumatic stress exposure may be accumulating "
                f"faster than processing (compression ratio={v.wisdom_compression_ratio:.2f}). "
                f"High emotional activation ({v.q:.2f}) with limited wisdom integration ({v.rho:.2f}) "
                f"may indicate need for supported meaning-making."
            ),
            CompassionState.BURNOUT_PRECURSOR: (
                f"Energy depletion patterns detected. "
                f"Cumulative grief load ({v.cumulative_grief_load:.2f}) exceeds current "
                f"wisdom compression capacity. "
                f"Support structures may help before burnout cascade."
            ),
            CompassionState.CRISIS: (
                f"Pattern intensity suggests immediate support warranted. "
                f"Compassion reserves critically low ({v.compassion_reserve:.0%}). "
                f"This is not a failure—it's a signal that the system needs care."
            )
        }
        
        return summaries.get(state, "Pattern requires further analysis.")
    
    def _generate_wisdom_pathway(self, v: PhysicianGCTVariables) -> str:
        """Generate suggested pathway for grief-to-wisdom transformation"""
        
        if v.wisdom_compression_ratio > 0.6:
            return (
                "Transformation already occurring. The suffering is finding meaning. "
                "Continue practices that support this integration—reflection, connection, "
                "allowing the accumulated wisdom to become accessible to others."
            )
        
        elif v.cumulative_grief_load > 0.5 and v.rho < 0.3:
            return (
                "Raw grief accumulated faster than processing capacity. "
                "Deliberate rumination (controlled revisiting vs. intrusive thoughts) "
                "may help transform weight into wisdom. "
                "Consider: What have these patients taught you about living? "
                "What would you want their families to know you learned from them?"
            )
        
        elif v.f < 0.3:
            return (
                "Isolation may be limiting transformation pathways. "
                "Social support is a key factor in post-traumatic growth. "
                "Sharing experiences with trusted colleagues can help construct "
                "new meaning from accumulated loss."
            )
        
        else:
            return (
                "Current patterns suggest normal grief processing. "
                "The jade forms under pressure—wisdom from suffering requires time "
                "and presence, not acceleration."
            )
    
    def _generate_support_suggestions(self, v: PhysicianGCTVariables,
                                      state: CompassionState) -> List[str]:
        """Generate support suggestions based on patterns"""
        
        suggestions = []
        
        if state == CompassionState.CRISIS:
            suggestions.extend([
                "Consider reaching out to a trusted colleague today",
                "Professional support available—this is not weakness but wisdom",
                "Rest is not abandonment of patients—it's preservation of capacity to serve"
            ])
        
        elif state == CompassionState.COMPASSION_FATIGUE:
            suggestions.extend([
                "Debrief support after particularly difficult cases may help",
                "The 'heaviness' you feel is shared by others who do this work",
                "Consider whether current load matches recovery capacity"
            ])
        
        elif state == CompassionState.BURNOUT_PRECURSOR:
            suggestions.extend([
                "Early intervention prevents cascade—now is the time",
                "What practices restore rather than merely distract?",
                "Permission to acknowledge the cost of this work"
            ])
        
        # Add based on specific variables
        if v.f < 0.3:
            suggestions.append(
                "Connection with others who understand may help—isolation compounds grief"
            )
        
        if v.tau > 0.6:
            suggestions.append(
                "Long temporal pattern—cumulative impact acknowledged. "
                "The weight of years deserves witness."
            )
        
        return suggestions
    
    def _calculate_confidence(self, v: PhysicianGCTVariables, text: str) -> float:
        """Calculate confidence in translation"""
        
        # Longer text = more signal = more confidence
        word_count = len(text.split())
        length_confidence = min(word_count / 100, 0.4)
        
        # More extreme variables = more confidence in detection
        variable_clarity = (abs(v.psi - 0.5) + abs(v.q - 0.5) + 
                          abs(v.rho - 0.5) + abs(v.f - 0.5)) / 2
        
        # Low lambda (low ambiguity) = higher confidence
        frame_confidence = (1 - v.lambda_coef) * 0.3
        
        return min(length_confidence + variable_clarity * 0.3 + frame_confidence, 0.85)
    
    def _generate_alternatives(self, v: PhysicianGCTVariables) -> List[str]:
        """Generate alternative readings of the pattern"""
        
        alternatives = []
        
        if v.q < 0.3:
            alternatives.append(
                "Low emotional activation could indicate protective presence OR "
                "concerning detachment—context and history needed to distinguish"
            )
        
        if v.psi > 0.7:
            alternatives.append(
                "High integration could reflect mature practice OR "
                "suppressed conflict between clinical and human responses"
            )
        
        if v.rho > 0.6:
            alternatives.append(
                "Strong wisdom markers could indicate genuine transformation OR "
                "intellectualization as defense against raw grief"
            )
        
        # Always include this
        alternatives.append(
            "This reading is through one lens—other calibrations may reveal "
            "different patterns equally present in the same expression"
        )
        
        return alternatives
    
    def _generate_uncertainty_notes(self, v: PhysicianGCTVariables) -> List[str]:
        """Generate explicit uncertainty acknowledgments"""
        
        notes = []
        
        if v.lambda_coef > 0.5:
            notes.append(
                "High frame ambiguity—clinical and personal dimensions mixing "
                "in ways that complicate interpretation"
            )
        
        # Always include fundamental uncertainty
        notes.append(
            "Coherence is constructed, not discovered. "
            "This translation reflects pattern visibility through this lens, "
            "not ground truth about internal states."
        )
        
        return notes
    
    def get_accumulation_trend(self) -> Optional[Dict[str, Any]]:
        """Analyze trend in accumulated translations"""
        
        if len(self.accumulation_history) < 3:
            return None
        
        recent = self.accumulation_history[-5:]
        
        # Calculate trends
        grief_trend = [v.cumulative_grief_load for v in recent]
        wisdom_trend = [v.rho for v in recent]
        reserve_trend = [v.compassion_reserve for v in recent]
        
        return {
            'grief_direction': 'increasing' if grief_trend[-1] > grief_trend[0] else 'stable_or_decreasing',
            'wisdom_direction': 'increasing' if wisdom_trend[-1] > wisdom_trend[0] else 'stable_or_decreasing',
            'reserve_direction': 'increasing' if reserve_trend[-1] > reserve_trend[0] else 'decreasing',
            'sample_size': len(recent),
            'note': "Trends are patterns, not predictions. Use as reflection prompt, not diagnosis."
        }
