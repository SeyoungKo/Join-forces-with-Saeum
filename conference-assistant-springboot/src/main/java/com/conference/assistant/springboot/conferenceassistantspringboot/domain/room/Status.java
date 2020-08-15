package com.conference.assistant.springboot.conferenceassistantspringboot.domain.room;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@Getter
@RequiredArgsConstructor
public enum Status {
    INVALID("STATUS_INVALID","삭제된방"),
    VALID("STATUS_VALID","유효한방");

    private final String key;
    private final String title;
}
