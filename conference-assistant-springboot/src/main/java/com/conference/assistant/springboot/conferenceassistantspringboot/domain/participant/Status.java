package com.conference.assistant.springboot.conferenceassistantspringboot.domain.participant;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@Getter
@RequiredArgsConstructor
public enum Status {
    ATTEND("STATUS_ATTEND","참여"),
    ABSENCE("STATUS_ABSENCE","불참");

    private final String key;
    private final String title;
}
