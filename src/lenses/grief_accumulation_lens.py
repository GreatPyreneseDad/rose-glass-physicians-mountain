"""
Grief Accumulation Lens
=======================

Tracks patterns of grief accumulation and transformation.

Distinguishes between:
- Raw grief (unprocessed, potentially harmful)
- Processed grief (acknowledged, integrated)
- Compressed wisdom (transformed into accessible knowledge)

Author: Christopher MacGregor bin Joseph
Date: December 2025
"""

from dataclasses import dataclass
from typing import List
from enum import Enum


class GriefState(Enum):
    """Current state of grief processing"""
    MINIMAL = "minimal"  # Low grief load
    RAW_ACCUMULATING = "raw_accumulating"  # Grief building without processing
    PROCESSING_ACTIVE = "processing_active"  # Actively working through grief
    INTEGRATING = "integrating"  # Finding meaning and integration
    COMPRESSED = "compressed"  # Transformed into wisdom


@dataclass
class GriefLensResult:
    """Result of viewing through grief accumulation lens"""
    state: GriefState
    raw_grief_level: float
    processed_grief_level: float
    compression_ratio: float  # How much has transformed to wisdom
    
    pattern_description: str
    transformation_status: str
    growth_indicators: List[str]
    concern_indicators: List[str]
    next_steps: List[str]


class GriefAccumulationLens:
    """
    Lens for tracking grief accumulation and transformation.
    
    Key insight: grief must be processed to become wisdom.
    Unprocessed grief accumulates as weight; processed grief
    compresses into accessible knowledge that can serve others.
    """
    
    def __init__(self):
        self.name = "Grief Accumulation Lens"
        
        # Markers for different grief states
        self.raw_grief_markers = [
            'lost', 'died', 'death', 'passed', 'gone',
            'another one', 'how many more', 'can\'t take this'
        ]
        
        self.processing_markers = [
            'thinking about', 'trying to understand', 'making sense',
            'working through', 'processing', 'grieving'
        ]
        
        self.wisdom_markers = [
            'learned', 'taught me', 'understand now', 'realize',
            'gift', 'grateful', 'meaning', 'purpose', 'transformed'
        ]
        
        self.growth_markers = [
            'stronger', 'deeper', 'more compassionate', 'appreciate',
            'perspective', 'changed', 'growth', 'enriched'
        ]
        
        self.concern_markers = [
            'overwhelmed', 'too much', 'can\'t handle', 'breaking',
            'numb', 'nothing left', 'empty', 'hollow'
        ]
    
    def view(self, text: str) -> GriefLensResult:
        """View text through grief accumulation lens"""
        
        text_lower = text.lower()
        word_count = len(text.split())
        
        if word_count == 0:
            return self._empty_result()
        
        # Calculate levels
        raw_level = self._calculate_raw_grief(text_lower, word_count)
        processed_level = self._calculate_processed_grief(text_lower, word_count)
        wisdom_level = self._calculate_wisdom_level(text_lower, word_count)
        
        # Calculate compression ratio
        total_grief = raw_level + processed_level + 0.01  # Avoid division by zero
        compression_ratio = wisdom_level / total_grief
        compression_ratio = min(compression_ratio, 1.0)
        
        # Determine state
        state = self._determine_state(raw_level, processed_level, wisdom_level)
        
        # Generate narrative elements
        pattern_desc = self._generate_description(state, raw_level, wisdom_level)
        transformation = self._assess_transformation(compression_ratio, state)
        
        # Identify indicators
        growth_indicators = self._identify_growth(text_lower)
        concern_indicators = self._identify_concerns(text_lower)
        
        # Generate next steps
        next_steps = self._generate_next_steps(state, raw_level, compression_ratio)
        
        return GriefLensResult(
            state=state,
            raw_grief_level=raw_level,
            processed_grief_level=processed_level,
            compression_ratio=compression_ratio,
            pattern_description=pattern_desc,
            transformation_status=transformation,
            growth_indicators=growth_indicators,
            concern_indicators=concern_indicators,
            next_steps=next_steps
        )
    
    def _calculate_raw_grief(self, text: str, word_count: int) -> float:
        """Calculate raw unprocessed grief level"""
        grief_count = sum(1 for m in self.raw_grief_markers if m in text)
        return min(grief_count / (word_count * 0.05 + 1), 1.0)
    
    def _calculate_processed_grief(self, text: str, word_count: int) -> float:
        """Calculate actively processing grief level"""
        process_count = sum(1 for m in self.processing_markers if m in text)
        return min(process_count / (word_count * 0.05 + 1), 1.0)
    
    def _calculate_wisdom_level(self, text: str, word_count: int) -> float:
        """Calculate wisdom/transformation level"""
        wisdom_count = sum(1 for m in self.wisdom_markers if m in text)
        growth_count = sum(1 for m in self.growth_markers if m in text)
        return min((wisdom_count + growth_count) / (word_count * 0.05 + 1), 1.0)
    
    def _determine_state(self, 
                        raw: float, 
                        processed: float, 
                        wisdom: float) -> GriefState:
        """Determine current grief state"""
        
        if raw < 0.2 and processed < 0.2 and wisdom < 0.2:
            return GriefState.MINIMAL
        
        if wisdom > 0.5 and raw < 0.3:
            return GriefState.COMPRESSED
        
        if processed > 0.4:
            if wisdom > 0.3:
                return GriefState.INTEGRATING
            return GriefState.PROCESSING_ACTIVE
        
        if raw > 0.3 and wisdom < 0.3:
            return GriefState.RAW_ACCUMULATING
        
        return GriefState.PROCESSING_ACTIVE  # Default
    
    def _generate_description(self, 
                             state: GriefState, 
                             raw: float, 
                             wisdom: float) -> str:
        """Generate narrative description"""
        
        descriptions = {
            GriefState.MINIMAL: (
                "Low grief markers detected. This may reflect low exposure, "
                "effective ongoing processing, or text that didn't capture grief content."
            ),
            GriefState.RAW_ACCUMULATING: (
                f"Raw grief level: {raw:.0%}. Grief appears to be accumulating "
                "faster than processing. This is common in high-volume settings "
                "but may benefit from dedicated processing time."
            ),
            GriefState.PROCESSING_ACTIVE: (
                "Active processing indicators present. The work of meaning-making "
                "appears to be underway. This is the path from weight to wisdom."
            ),
            GriefState.INTEGRATING: (
                "Integration occurring. Grief is finding its place alongside "
                "purpose and meaning. This is post-traumatic growth in process."
            ),
            GriefState.COMPRESSED: (
                f"Wisdom level: {wisdom:.0%}. Significant transformation evident. "
                "Grief has compressed into accessible knowledge. "
                "This wisdom can now serve others."
            )
        }
        
        return descriptions.get(state, "State requires further analysis.")
    
    def _assess_transformation(self, ratio: float, state: GriefState) -> str:
        """Assess transformation progress"""
        
        if state == GriefState.COMPRESSED:
            return (
                "Transformation largely complete. The jade has formed. "
                "The compressed wisdom from this suffering can now benefit others."
            )
        
        if ratio > 0.6:
            return "Strong transformation occurring. Grief becoming wisdom."
        elif ratio > 0.3:
            return "Transformation in progress. Some grief processing effectively."
        elif ratio > 0.1:
            return "Early transformation. Processing capacity may need support."
        else:
            return "Limited transformation detected. Deliberate processing may help."
    
    def _identify_growth(self, text: str) -> List[str]:
        """Identify post-traumatic growth indicators"""
        
        indicators = []
        
        for marker in self.growth_markers:
            if marker in text:
                indicator_texts = {
                    'stronger': "Increased sense of personal strength",
                    'deeper': "Deepened capacity for connection/understanding",
                    'more compassionate': "Enhanced compassion capacity",
                    'appreciate': "Greater appreciation for life/relationships",
                    'perspective': "Changed life priorities or perspective",
                    'changed': "Transformation in sense of self or values",
                    'growth': "Explicit recognition of growth from adversity",
                    'enriched': "Sense of enrichment from difficult experience"
                }
                if marker in indicator_texts:
                    indicators.append(indicator_texts[marker])
        
        return indicators
    
    def _identify_concerns(self, text: str) -> List[str]:
        """Identify concerning patterns"""
        
        concerns = []
        
        for marker in self.concern_markers:
            if marker in text:
                concern_texts = {
                    'overwhelmed': "Overwhelm signals may indicate capacity exceeded",
                    'too much': "Sense of excessive load present",
                    'can\'t handle': "Coping capacity may be strained",
                    'breaking': "Risk of decompensation indicated",
                    'numb': "Emotional numbing as protective mechanism",
                    'nothing left': "Depletion signals present",
                    'empty': "Emotional exhaustion indicated",
                    'hollow': "Sense of emptiness or disconnection"
                }
                if marker in concern_texts:
                    concerns.append(concern_texts[marker])
        
        return concerns
    
    def _generate_next_steps(self, 
                            state: GriefState, 
                            raw: float,
                            ratio: float) -> List[str]:
        """Generate recommended next steps"""
        
        steps = []
        
        if state == GriefState.RAW_ACCUMULATING:
            steps.extend([
                "Consider dedicated time for grief processing",
                "Deliberate rumination (controlled, time-bounded) may help",
                "Sharing with trusted colleague can facilitate processing"
            ])
        
        elif state == GriefState.PROCESSING_ACTIVE:
            steps.extend([
                "Continue processing work—transformation underway",
                "Ask: What is this loss teaching me?",
                "Consider what wisdom could serve others"
            ])
        
        elif state == GriefState.INTEGRATING:
            steps.extend([
                "Integration occurring—continue supportive practices",
                "Notice how this loss has changed your practice",
                "Consider sharing insights with others in similar work"
            ])
        
        elif state == GriefState.COMPRESSED:
            steps.extend([
                "Consider sharing accumulated wisdom with colleagues",
                "This transformation can benefit those earlier in the journey",
                "Mentorship role may be natural extension of this growth"
            ])
        
        return steps
    
    def _empty_result(self) -> GriefLensResult:
        """Return result for empty input"""
        return GriefLensResult(
            state=GriefState.MINIMAL,
            raw_grief_level=0.0,
            processed_grief_level=0.0,
            compression_ratio=0.0,
            pattern_description="No text to analyze",
            transformation_status="Insufficient data",
            growth_indicators=[],
            concern_indicators=[],
            next_steps=[]
        )
