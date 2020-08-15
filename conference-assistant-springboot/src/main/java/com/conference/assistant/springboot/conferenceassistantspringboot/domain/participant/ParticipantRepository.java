package com.conference.assistant.springboot.conferenceassistantspringboot.domain.participant;

import org.springframework.data.jpa.repository.JpaRepository;

public interface ParticipantRepository extends JpaRepository<Participant, Long> {
}
