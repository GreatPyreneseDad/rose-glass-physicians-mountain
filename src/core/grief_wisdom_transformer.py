"""
Grief to Wisdom Transformer
===========================

Implements the core transformation pipeline for converting accumulated
medical grief into accessible wisdom patterns.

Based on:
- Tedeschi & Calhoun's Post-Traumatic Growth framework
- Viktor Frankl's meaning-making approach
- Research on deliberate vs. intrusive rumination

Author: Christopher MacGregor bin Joseph  
Date: December 2025
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from datetime import datetime
from enum import Enum
import math


class GriefPhase(Enum):
    """Phases in grief-to-wisdom transformation"""
    RAW = "raw"  # Unprocessed, intrusive
    ACKNOWLEDGED = "acknowledged"  # Recognized but not integrated
    PROCESSING = "processing"  # Active deliberate rumination
    INTEGRATING = "integrating"  # Finding meaning
    COMPRESSED = "compressed"  # Transformed into accessible wisdom


class WisdomType(Enum):
    """Types of wisdom that can emerge from grief"""
    PRESENCE = "presence"  # How to be with suffering
    COMMUNICATION = "communication"  # What to say, what not to say
    COMPASSION = "compassion"  # Deeper capacity for connection
    PERSPECTIVE = "perspective"  # Life priorities, what matters
    RESILIENCE = "resilience"  # Capacity to endure
    SERVICE = "service"  # How to help others through similar experiences


@dataclass
class GriefEvent:
    """A grief-inducing event in physician experience"""
    event_id: str
    timestamp: datetime
    patient_type: str  # pediatric, adult, elderly
    relationship_depth: float  # 0-1 how connected
    circumstances: List[str]  # sudden, prolonged, complicated
    initial_intensity: float  # 0-1 raw grief intensity
    
    # Transformation tracking
    current_phase: GriefPhase = GriefPhase.RAW
    wisdom_extracted: List[WisdomType] = field(default_factory=list)
    processing_attempts: int = 0
    last_processed: Optional[datetime] = None


@dataclass
class WisdomFragment:
    """A piece of wisdom extracted from grief"""
    wisdom_type: WisdomType
    source_events: List[str]  # Event IDs that contributed
    insight: str
    accessibility: float  # 0-1 how readily available
    shareable: bool  # Can be shared with others
    extraction_date: datetime = field(default_factory=datetime.now)


@dataclass 
class TransformationResult:
    """Result of a transformation session"""
    grief_events_processed: int
    wisdom_generated: List[WisdomFragment]
    rho_change: float  # Change in accumulated wisdom
    remaining_load: float
    pathway_used: str
    reflections: List[str]
    next_steps: List[str]


class DeliberateRuminationGuide:
    """
    Guides controlled revisiting of grief events to facilitate
    transformation into wisdom.
    
    Distinct from intrusive rumination (which perpetuates distress),
    deliberate rumination is purposeful, time-bounded, and
    meaning-seeking.
    """
    
    PRESENCE_PROMPTS = [
        "What did this patient teach you about being with suffering?",
        "What would you do differently in how you showed up?",
        "What did their presence reveal about your own capacity for presence?"
    ]
    
    COMMUNICATION_PROMPTS = [
        "What words mattered most to the family?",
        "What did you wish you had said? What are you glad you said?",
        "What did their silence or their questions teach you?"
    ]
    
    COMPASSION_PROMPTS = [
        "How did this experience change your capacity for connection?",
        "What about this loss keeps you human?",
        "What would it mean to honor their memory through your practice?"
    ]
    
    PERSPECTIVE_PROMPTS = [
        "What does this loss illuminate about what matters?",
        "How does this patient's life inform how you want to live yours?",
        "What would they want you to take forward from knowing them?"
    ]
    
    RESILIENCE_PROMPTS = [
        "What helped you continue after this loss?",
        "What resources—internal or external—did you draw on?",
        "What would you tell another physician facing similar loss?"
    ]
    
    SERVICE_PROMPTS = [
        "What can you offer others because of what you learned here?",
        "How does this grief equip you to serve others in grief?",
        "What wisdom could be shared without betraying the sacred?"
    ]
    
    def get_prompts(self, wisdom_type: WisdomType) -> List[str]:
        """Get prompts for deliberate rumination toward specific wisdom type"""
        prompt_maps = {
            WisdomType.PRESENCE: self.PRESENCE_PROMPTS,
            WisdomType.COMMUNICATION: self.COMMUNICATION_PROMPTS,
            WisdomType.COMPASSION: self.COMPASSION_PROMPTS,
            WisdomType.PERSPECTIVE: self.PERSPECTIVE_PROMPTS,
            WisdomType.RESILIENCE: self.RESILIENCE_PROMPTS,
            WisdomType.SERVICE: self.SERVICE_PROMPTS
        }
        return prompt_maps.get(wisdom_type, self.PERSPECTIVE_PROMPTS)


class GriefWisdomTransformer:
    """
    Main transformation engine for converting grief into wisdom.
    
    Core principle: Suffering encountered with presence becomes wisdom;
    suffering avoided or suppressed accumulates as weight.
    """
    
    def __init__(self):
        self.grief_registry: Dict[str, GriefEvent] = {}
        self.wisdom_bank: List[WisdomFragment] = []
        self.rumination_guide = DeliberateRuminationGuide()
        
        # Transformation parameters
        self.processing_threshold = 3  # Attempts before integration possible
        self.compression_rate = 0.15  # How much grief converts per session
    
    def register_grief_event(self, event: GriefEvent) -> str:
        """Register a new grief event for tracking"""
        self.grief_registry[event.event_id] = event
        return event.event_id
    
    def get_current_load(self) -> float:
        """Calculate current cumulative grief load"""
        total_load = 0.0
        for event in self.grief_registry.values():
            # Unprocessed grief contributes more to load
            phase_weights = {
                GriefPhase.RAW: 1.0,
                GriefPhase.ACKNOWLEDGED: 0.8,
                GriefPhase.PROCESSING: 0.5,
                GriefPhase.INTEGRATING: 0.3,
                GriefPhase.COMPRESSED: 0.1
            }
            weight = phase_weights.get(event.current_phase, 0.5)
            total_load += event.initial_intensity * weight * event.relationship_depth
        
        return min(total_load / 10, 1.0)  # Normalize to 0-1
    
    def get_current_rho(self) -> float:
        """Calculate current accumulated wisdom (ρ)"""
        if not self.wisdom_bank:
            return 0.0
        
        total_wisdom = sum(w.accessibility for w in self.wisdom_bank)
        return min(total_wisdom / 10, 1.0)
    
    def get_compression_ratio(self) -> float:
        """Calculate how much grief has transformed to wisdom"""
        total_grief = sum(e.initial_intensity * e.relationship_depth 
                        for e in self.grief_registry.values())
        if total_grief == 0:
            return 0.5  # No grief to process
        
        total_wisdom = sum(w.accessibility for w in self.wisdom_bank)
        return min(total_wisdom / total_grief, 1.0)
    
    def identify_transformation_candidates(self, max_candidates: int = 3) -> List[GriefEvent]:
        """Identify grief events ready for transformation work"""
        candidates = []
        
        for event in self.grief_registry.values():
            # Skip already compressed events
            if event.current_phase == GriefPhase.COMPRESSED:
                continue
            
            # Prioritize events that have been acknowledged but not processed
            # and events with sufficient processing attempts
            score = 0.0
            
            if event.current_phase == GriefPhase.ACKNOWLEDGED:
                score += 0.3
            elif event.current_phase == GriefPhase.PROCESSING:
                score += 0.5
            elif event.current_phase == GriefPhase.INTEGRATING:
                score += 0.4
            
            # Higher relationship depth = more transformation potential
            score += event.relationship_depth * 0.3
            
            # Events that haven't been touched recently
            if event.last_processed:
                days_since = (datetime.now() - event.last_processed).days
                if days_since > 7:
                    score += 0.2
            else:
                score += 0.1  # Never processed
            
            candidates.append((event, score))
        
        # Sort by score descending
        candidates.sort(key=lambda x: x[1], reverse=True)
        return [c[0] for c in candidates[:max_candidates]]
    
    def suggest_wisdom_pathway(self, event: GriefEvent) -> Tuple[WisdomType, List[str]]:
        """Suggest which wisdom type to pursue and provide prompts"""
        
        # Determine which wisdom types haven't been extracted yet
        available_types = [t for t in WisdomType if t not in event.wisdom_extracted]
        
        if not available_types:
            # All types extracted—cycle back to presence
            suggested_type = WisdomType.PRESENCE
        else:
            # Prioritize based on event characteristics
            if 'sudden' in event.circumstances:
                suggested_type = WisdomType.RESILIENCE if WisdomType.RESILIENCE in available_types else available_types[0]
            elif 'prolonged' in event.circumstances:
                suggested_type = WisdomType.COMPASSION if WisdomType.COMPASSION in available_types else available_types[0]
            elif event.patient_type == 'pediatric':
                suggested_type = WisdomType.PERSPECTIVE if WisdomType.PERSPECTIVE in available_types else available_types[0]
            else:
                suggested_type = available_types[0]
        
        prompts = self.rumination_guide.get_prompts(suggested_type)
        return suggested_type, prompts
    
    def process_reflection(self, event_id: str, 
                          reflection_text: str,
                          wisdom_type: WisdomType) -> TransformationResult:
        """
        Process a deliberate reflection on a grief event.
        
        This is where transformation happens—the physician engages
        with the grief through controlled rumination, and the system
        facilitates extraction of wisdom.
        """
        
        if event_id not in self.grief_registry:
            raise ValueError(f"Unknown event: {event_id}")
        
        event = self.grief_registry[event_id]
        
        # Update processing state
        event.processing_attempts += 1
        event.last_processed = datetime.now()
        
        # Advance phase if appropriate
        if event.current_phase == GriefPhase.RAW:
            event.current_phase = GriefPhase.ACKNOWLEDGED
        elif event.current_phase == GriefPhase.ACKNOWLEDGED and event.processing_attempts >= 2:
            event.current_phase = GriefPhase.PROCESSING
        elif event.current_phase == GriefPhase.PROCESSING and event.processing_attempts >= self.processing_threshold:
            event.current_phase = GriefPhase.INTEGRATING
        
        # Extract wisdom from reflection
        wisdom = self._extract_wisdom_from_reflection(
            reflection_text, 
            wisdom_type,
            [event_id]
        )
        
        if wisdom:
            self.wisdom_bank.append(wisdom)
            event.wisdom_extracted.append(wisdom_type)
            
            # Check if enough wisdom extracted for compression
            if len(event.wisdom_extracted) >= 3:
                event.current_phase = GriefPhase.COMPRESSED
        
        # Calculate changes
        new_load = self.get_current_load()
        new_rho = self.get_current_rho()
        
        # Generate reflections and next steps
        reflections = self._generate_transformation_reflections(event, wisdom_type)
        next_steps = self._generate_next_steps(event)
        
        return TransformationResult(
            grief_events_processed=1,
            wisdom_generated=[wisdom] if wisdom else [],
            rho_change=0.1 if wisdom else 0.0,  # Approximate
            remaining_load=new_load,
            pathway_used=wisdom_type.value,
            reflections=reflections,
            next_steps=next_steps
        )
    
    def _extract_wisdom_from_reflection(self, 
                                        text: str,
                                        wisdom_type: WisdomType,
                                        source_events: List[str]) -> Optional[WisdomFragment]:
        """Extract wisdom fragment from reflection text"""
        
        # Check for wisdom indicators
        wisdom_markers = {
            WisdomType.PRESENCE: ['being with', 'showed up', 'present', 'stayed'],
            WisdomType.COMMUNICATION: ['said', 'told', 'words', 'listen', 'heard'],
            WisdomType.COMPASSION: ['feel', 'connect', 'human', 'heart', 'care'],
            WisdomType.PERSPECTIVE: ['realize', 'understand', 'matter', 'important', 'life'],
            WisdomType.RESILIENCE: ['continue', 'strength', 'endure', 'carry on', 'cope'],
            WisdomType.SERVICE: ['help', 'share', 'teach', 'guide', 'support']
        }
        
        markers = wisdom_markers.get(wisdom_type, [])
        text_lower = text.lower()
        marker_count = sum(1 for m in markers if m in text_lower)
        
        # Need some markers to extract wisdom
        if marker_count < 2:
            return None
        
        # Calculate accessibility based on clarity and depth
        word_count = len(text.split())
        accessibility = min(word_count / 100, 0.8) + (marker_count * 0.05)
        
        # Determine if shareable (contains generalizable insight)
        shareable_markers = ['others', 'anyone', 'people', 'colleagues', 'we']
        shareable = any(m in text_lower for m in shareable_markers)
        
        return WisdomFragment(
            wisdom_type=wisdom_type,
            source_events=source_events,
            insight=self._summarize_insight(text, wisdom_type),
            accessibility=min(accessibility, 1.0),
            shareable=shareable
        )
    
    def _summarize_insight(self, text: str, wisdom_type: WisdomType) -> str:
        """Generate brief insight summary from reflection"""
        
        # In production, this would use NLP. For now, template-based.
        templates = {
            WisdomType.PRESENCE: "Learned to be present with suffering in new ways",
            WisdomType.COMMUNICATION: "Discovered what words matter when facing loss",
            WisdomType.COMPASSION: "Deepened capacity for human connection through shared grief",
            WisdomType.PERSPECTIVE: "Gained clarity on what matters through witnessing loss",
            WisdomType.RESILIENCE: "Found inner resources to continue serving through difficulty",
            WisdomType.SERVICE: "Discovered how grief equips us to help others"
        }
        
        return templates.get(wisdom_type, "Wisdom extracted through reflection")
    
    def _generate_transformation_reflections(self, 
                                            event: GriefEvent,
                                            wisdom_type: WisdomType) -> List[str]:
        """Generate reflections on the transformation process"""
        
        reflections = []
        
        if event.current_phase == GriefPhase.COMPRESSED:
            reflections.append(
                f"This loss has moved through transformation. "
                f"The grief has compressed into wisdom that can serve others."
            )
        elif event.current_phase == GriefPhase.INTEGRATING:
            reflections.append(
                f"Integration is occurring. The loss is becoming part of "
                f"your expanded capacity rather than just weight carried."
            )
        else:
            reflections.append(
                f"Processing continues. Each deliberate return adds to transformation."
            )
        
        # Wisdom-type specific reflections
        type_reflections = {
            WisdomType.PRESENCE: "The capacity to be with suffering grows with each encounter honored.",
            WisdomType.COMMUNICATION: "Words found in grief's depth often reach others facing similar shadows.",
            WisdomType.COMPASSION: "The heart broken open by loss holds more, not less.",
            WisdomType.PERSPECTIVE: "Loss clarifies what matters—a gift wrapped in darkness.",
            WisdomType.RESILIENCE: "Each passage through grief maps the terrain for those who follow.",
            WisdomType.SERVICE: "What you extract from your suffering becomes medicine for others."
        }
        
        if wisdom_type in type_reflections:
            reflections.append(type_reflections[wisdom_type])
        
        return reflections
    
    def _generate_next_steps(self, event: GriefEvent) -> List[str]:
        """Generate suggested next steps for transformation"""
        
        steps = []
        
        if event.current_phase == GriefPhase.RAW:
            steps.append("Allow acknowledgment without forcing processing")
            steps.append("Notice when this loss surfaces—these are invitations, not intrusions")
        
        elif event.current_phase == GriefPhase.ACKNOWLEDGED:
            steps.append("When ready, consider which dimension of wisdom this loss offers")
            steps.append("Short, time-bounded deliberate reflection more helpful than extended rumination")
        
        elif event.current_phase == GriefPhase.PROCESSING:
            steps.append("Continue deliberate engagement—transformation is in process")
            steps.append("Consider sharing insights with trusted colleague")
        
        elif event.current_phase == GriefPhase.INTEGRATING:
            steps.append("Notice how this loss has changed your practice")
            steps.append("The wisdom is becoming accessible—let it inform how you serve")
        
        elif event.current_phase == GriefPhase.COMPRESSED:
            steps.append("This transformation is largely complete")
            steps.append("The wisdom can now be shared without re-opening the wound")
        
        # Check for types not yet extracted
        remaining_types = [t for t in WisdomType if t not in event.wisdom_extracted]
        if remaining_types and event.current_phase not in [GriefPhase.RAW, GriefPhase.COMPRESSED]:
            steps.append(f"Consider exploring: {remaining_types[0].value}")
        
        return steps
    
    def get_wisdom_inventory(self) -> Dict[str, List[WisdomFragment]]:
        """Get all accumulated wisdom organized by type"""
        inventory = {t.value: [] for t in WisdomType}
        
        for wisdom in self.wisdom_bank:
            inventory[wisdom.wisdom_type.value].append(wisdom)
        
        return inventory
    
    def get_shareable_wisdom(self) -> List[WisdomFragment]:
        """Get wisdom fragments that can be shared with others"""
        return [w for w in self.wisdom_bank if w.shareable]
