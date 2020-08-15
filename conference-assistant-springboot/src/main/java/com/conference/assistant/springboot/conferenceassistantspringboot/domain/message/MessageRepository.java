package com.conference.assistant.springboot.conferenceassistantspringboot.domain.message;

import org.springframework.data.jpa.repository.JpaRepository;

public interface MessageRepository extends JpaRepository<Message, Long> {
}
